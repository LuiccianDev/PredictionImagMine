from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from backend.database.database_model import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid
class LabelBase:
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    prediction_id = Column(UUID(as_uuid=True), ForeignKey("predictions.id", ondelete="CASCADE"))
    real_label = Column(String(100), nullable=False)
    feedback = Column(Boolean, nullable=False)
    timestamp = Column(TIMESTAMP, default=func.current_timestamp())


# Definición para PostgreSQL
class LabelPostgres(Base, LabelBase):
    __tablename__ = "labels"
    
    predictions = relationship('PredictionPostgres', backref='labels', lazy=True)

