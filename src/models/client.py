from sqlalchemy import Column, String, Integer,ForeignKey ,Boolean
from sqlalchemy.orm import relationship
from src.config.database import Base

class Client(Base):
    __tablename__ = 'client'
    identification = Column(String, primary_key=True)
    name = Column(String(length=100), nullable=False)
    lastname = Column(String(length=100), nullable=False)
    status = Column(Boolean, nullable=False, default=True)
    address = Column(Integer, ForeignKey('rol.id'),nullable=False )
    email = Column(String(length=100), nullable=False, unique=True)
    id_company = Column(Integer,ForeignKey('company.id') ,nullable=False)
    id_city = Column(Integer, ForeignKey('city.id'), nullable=False)
    Rcompany = relationship("Company", back_populates="Rclient")
    Rcity = relationship("City", back_populates="Rclient")
    Rbill = relationship("Bill", back_populates="Rclient")
