from flask import request, jsonify
import jwt
from functools import wraps  # Necesario para que el decorador funcione correctamente
from backend.config import SECRET_KEY  # Asegúrate de importar la clave correctamente
from backend.models.user  import UserPostgreSQL

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get("Authorization")

        if not token:
            return jsonify({"error": "Token faltante"}), 401
        
        # Manejo del formato "Bearer <TOKEN>"
        parts = token.split()
        if len(parts) != 2 or parts[0].lower() != "bearer":
            return jsonify({"error": "Formato de token inválido"}), 401

        try:
            data = jwt.decode(parts[1], SECRET_KEY, algorithms=["HS256"])
            user = UserPostgreSQL.query.get(data["user_id"])  # Buscar usuario en la base de datos
            
            if not user:
                return jsonify({"error": "Usuario no encontrado"}), 401

            return f(*args, **kwargs, current_user=user)  # Pasa el usuario a la función decorada
        except jwt.ExpiredSignatureError:
            return jsonify({"error": "Token expirado"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"error": "Token inválido"}), 401
        except Exception as e:
            return jsonify({"error": f"Error inesperado: {str(e)}"}), 500

    return decorated
