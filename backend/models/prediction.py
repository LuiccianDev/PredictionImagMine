
from sqlalchemy import Column, Integer, String, Float, TIMESTAMP, ForeignKey, Boolean
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from backend.database.database_model import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid
class PredictionBase:
    """Mixin con los campos comunes para la tabla de predicciones."""
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    image_name = Column(String(255), nullable=False)
    image_path = Column(String(255), nullable=False)
    predicted_mineral = Column(String(100), nullable=False)
    confidence = Column(Float, nullable=False)
    timestamp = Column(TIMESTAMP, server_default=func.current_timestamp()) 
    source = Column(String(100), nullable=True)
    processing_time = Column(Float, nullable=True)
    model_version = Column(String(50), nullable=True)
    feedback = Column(Boolean, nullable=True)
    real_label = Column(String(100), nullable=True)
    location_id = Column(UUID(as_uuid=True), ForeignKey("locations.id", ondelete="SET NULL"), nullable=True)
    device_id = Column(UUID(as_uuid=True), ForeignKey("devices.id", ondelete="SET NULL"), nullable=True)
    
    def compute_confidence_category(self):
        """Método para calcular la categoría de confianza."""
        if self.confidence >= 0.8:
            return "Alta"
        elif self.confidence >= 0.5:
            return "Media"
        else:
            return "Baja"
    
    @property
    def confidence_category(self):
        """Propiedad para acceder a la categoría de confianza."""
        return self.compute_confidence_category()


# ✅ Clase correcta para PostgreSQL
class PredictionPostgres(Base, PredictionBase):
    __tablename__ = "predictions"
    # Usando JSONB en lugar de JSON para mejorar el rendimiento en PostgreSQL
    metadata_data = Column(JSONB,nullable=True)  # JSONB es más eficiente en PostgreSQL
    user = relationship('UserPostgreSQL',  back_populates='predictions', lazy=True)
    location = relationship('LocationPostgreSQL', backref='predictions', lazy=True)
    device = relationship('DevicePostgreSQL', backref='predictions', lazy=True)

    
