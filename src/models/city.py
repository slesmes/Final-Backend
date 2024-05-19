from sqlalchemy import Column, String, Integer,ForeignKey ,Boolean
from sqlalchemy.orm import relationship
from src.config.database import Base

class City(Base):
    __tablename__ = 'city'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=100), nullable=False, unique=True)
    id_department = Column(Integer, ForeignKey('department.id'), nullable=False )
    Rdepartment = relationship("Department", back_populates="Rcity")
    Rcompany = relationship("Company", back_populates="Rcity")
    Rbranch = relationship("Branch", back_populates="Rcity")
    Rclient = relationship("Client", back_populates="Rcity")
