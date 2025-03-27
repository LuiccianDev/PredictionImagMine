from backend.database.database import SessionLocal
from backend.models.user import UserPostgreSQL
from sqlalchemy.exc import IntegrityError

class UserService:
    @staticmethod
    def get_user_profile(user_id):
        """Obtiene la información del perfil de un usuario."""
        with SessionLocal() as db:
            user = db.query(UserPostgreSQL).filter_by(id=user_id).first()
            if not user:
                return None
            return {
                "username": user.username,
                "email": user.email,
            }

    @staticmethod
    def update_user_profile(user_id, username, email):
        """Actualiza la información del perfil de un usuario."""
        with SessionLocal() as db:
            user = db.query(UserPostgreSQL).filter_by(id=user_id).first()
            if not user:
                return None

            # Actualizar los campos
            user.username = username
            user.email = email

            try:
                db.commit()
                return {
                    "username": user.username,
                    "email": user.email,
                }
            except IntegrityError:
                db.rollback()
                raise ValueError("El correo electrónico ya está en uso.")