from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from src.config.database import Base

class Department(Base):
    __tablename__ = 'department'
    id = Column(int, primary_key=True, autoincrement=True)
    name = Column(String(length=100), nullable=False, unique=True)
    id_country = Column(Integer, ForeignKey('country.id'), nullable=False)
    Rcountry = relationship("Country", back_populates="Rdepartment")
    Rcity = relationship("City", back_populates="Rdepartment")
