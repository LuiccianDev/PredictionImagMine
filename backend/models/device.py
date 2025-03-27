from sqlalchemy import Column, Integer, String, TIMESTAMP, func
from backend.database.database_model import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid
class DeviceBase:
    """Clase base con atributos comunes"""
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    device_name = Column(String(100), nullable=False)
    device_type = Column(String(50))
    created_at = Column(TIMESTAMP, server_default=func.now())

# PostgreSQL
class DevicePostgreSQL(Base, DeviceBase):
    __tablename__ = "devices"

