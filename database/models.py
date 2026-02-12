"""SQLAlchemy schema models for GridGuard AI."""

from sqlalchemy import Column, DateTime, Float, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, nullable=False)
    model = Column(String, nullable=False)
    predicted_load = Column(Float, nullable=False)
    confidence = Column(Float, nullable=False)
