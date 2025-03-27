import jwt
from jwt import ExpiredSignatureError, InvalidTokenError
from datetime import datetime, timedelta, timezone
from sqlalchemy.exc import IntegrityError
from werkzeug.security import check_password_hash, generate_password_hash
from backend.database.database import SessionLocal
from backend.models.user import UserPostgreSQL
from backend.config import SECRET_KEY
from backend.utils.logger import logger  

class AuthServices:
    
    @staticmethod
    def authenticate(username, password):
        """Autentica al usuario y genera un token JWT si las credenciales son correctas."""
        logger.info(f"Intento de autenticación para usuario: {username}")

        with SessionLocal() as db:
            try:
                user = db.query(UserPostgreSQL).filter_by(username=username).first()

                if not user:
                    logger.warning(f"Usuario {username} no encontrado.")
                    return {"error": "Usuario o contraseña incorrectos"}, 401

                # 🔹 Comparar contraseña en hash correctamente
                if not check_password_hash(user.password_hash, password):  
                    logger.warning(f"Contraseña incorrecta para usuario {username}")
                    return {"error": "Usuario o contraseña incorrectos"}, 401

                # 🔹 Generar token JWT
                token = jwt.encode(
                    {
                        "user_id": str(user.id),
                        "username": user.username,
                        "email": user.email,
                        "exp": datetime.now(timezone.utc) + timedelta(hours=2)
                    },
                    SECRET_KEY,
                    algorithm="HS256"
                )
                 # 🔹 Devolver token + datos del usuario
                return {
                    "token": token,
                    "user": {
                        "id": str(user.id),
                        "username": user.username,
                        "email": user.email
                    }
                }, 200

                """ logger.info(f"Autenticación exitosa para usuario: {username}")
                return {"token": token}, 200 """

            except Exception as e:
                logger.error(f"Error en autenticación para usuario {username}: {str(e)}", exc_info=True)
                return {"error": "Error interno del servidor"}, 500

    @staticmethod
    def signup(username, email, password):
        """Registra un nuevo usuario en la base de datos."""
        logger.info(f"Intento de registro para usuario: {username}")

        with SessionLocal() as db:
            try:
                # Encriptar la contraseña
                password_hash = generate_password_hash(password)

                # Crear el nuevo usuario
                new_user = UserPostgreSQL(username=username, email=email, password_hash=password_hash)
                db.add(new_user)
                db.commit()
                db.refresh(new_user)

                logger.info(f"Usuario registrado exitosamente: {username} con ID {new_user.id}")
                return {"message": "Usuario registrado exitosamente"}, 201

            except IntegrityError:
                db.rollback()
                logger.warning(f"Usuario o correo ya existente: {username}, {email}")
                return {"error": "El usuario o email ya están registrados"}, 409

            except Exception as e:
                db.rollback()
                logger.error(f"Error en registro para usuario {username}: {str(e)}", exc_info=True)
                return {"error": "Error interno del servidor"}, 500
            
    @staticmethod
    def get_user(token):
        """Obtiene la información del usuario autenticado a partir del token JWT."""
        try:
            # 🔹 Decodificar el token
            payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            user_id = payload.get("user_id")

            if not user_id:
                logger.warning("El token no contiene un user_id válido.")
                return {"error": "Token inválido"}, 401

            # 🔹 Consultar la base de datos
            with SessionLocal() as db:
                user = db.query(UserPostgreSQL).filter_by(id=user_id).first()

                if not user:
                    logger.warning(f"Usuario con ID {user_id} no encontrado.")
                    return {"error": "Usuario no encontrado"}, 404

                # 🔹 Retornar información del usuario
                return {
                    "user": {
                        "id": str(user.id),
                        "username": user.username,
                        "email": user.email
                    }
                }, 200

        except ExpiredSignatureError:
            logger.warning("Token expirado.")
            return {"error": "El token ha expirado"}, 401

        except InvalidTokenError:
            logger.warning("Token inválido.")
            return {"error": "Token inválido"}, 401

        except Exception as e:
            logger.error(f"Error al obtener usuario: {str(e)}", exc_info=True)
            return {"error": "Error interno del servidor"}, 500
