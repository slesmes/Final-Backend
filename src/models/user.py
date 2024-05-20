from sqlalchemy import Column, String, Integer,ForeignKey ,Boolean
from sqlalchemy.orm import relationship
from src.config.database import Base

class User(Base):
    __tablename__ = 'user'
    identification = Column(String(length=100), primary_key=True)
    name = Column(String(length=100), nullable=False)
    lastname = Column(String(length=100), nullable=False)
    username = Column(String(length=100), nullable=False)
    password = Column(String(length=100), nullable=False)
    phone = Column(String(length=100), nullable=False)
    status = Column(Boolean, nullable=False, default=True)
    email = Column(String(length=100), nullable=False, unique=True)
    id_branch = Column(Integer,ForeignKey('branch.id') ,nullable=False)
    id_rol = Column(Integer, ForeignKey('rol.id'),nullable=False )
    Rbranch = relationship("Branch", back_populates="Ruser")
    Rrol = relationship("Rol", back_populates="Ruser")
Rbill = relationship("Bill", back_populates="Ruser")


