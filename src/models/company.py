from sqlalchemy import Column, String, Integer,ForeignKey ,Boolean
from sqlalchemy.orm import relationship
from src.config.database import Base

class Company(Base):
    __tablename__ = 'company'
    nit = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=100), nullable=False, unique=True)
    address = Column(String(length=100), nullable=False )
    phone = Column(String(length=100), nullable=False )
    id_city = Column(Integer, ForeignKey('city.id'), nullable=False )
    status = Column(Boolean, nullable=False, default=True )
    Rcity = relationship("City", back_populates="Rcompany")
Rbranch = relationship("Branch", back_populates="Rcompany")
Rclient = relationship("Client", back_populates="Rcompany")