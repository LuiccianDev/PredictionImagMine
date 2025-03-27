from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from backend.database.database_model import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid
# Definición de la clase base
class UserBase:
    """Clase base con atributos comunes para usuarios"""
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    username = Column(String(100), nullable=False, unique=True)
    email = Column(String(150), nullable=False, unique=True)
    password_hash = Column(String(255), nullable=False)
    created_at = Column(DateTime, server_default=func.now())

# Clase que hereda de UserBase y usa SQLAlchemy
class UserPostgreSQL(Base, UserBase):
    __tablename__ = 'users'

    # Relación con otras tablas (si es necesario)
    predictions = relationship('PredictionPostgres',  back_populates="user", lazy=True)

    
