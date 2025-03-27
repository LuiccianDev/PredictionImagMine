from sqlalchemy import Column, Integer, String, Float, TIMESTAMP, func
from backend.database.database_model import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid
class LocationBase:
    """Clase base con atributos comunes"""
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String(50), nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())
    country = Column(String(50), nullable=False)

# PostgreSQL
class LocationPostgreSQL(Base, LocationBase):
    __tablename__ = "locations"

