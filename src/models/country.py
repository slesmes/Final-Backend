from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.orm import relationship
from src.config.database import Base

class Country(Base):
    __tablename__ = 'country'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=100), nullable=False, unique=True)
    Rdepartment = relationship("Department", back_populates="Rcountry")
