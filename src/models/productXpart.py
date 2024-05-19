from sqlalchemy import Column, String, Integer,ForeignKey ,Boolean
from sqlalchemy.orm import relationship
from src.config.database import Base

class Productxpart(Base):
    __tablename__ = 'productxpart'
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_supplier = Column(String(length=100), nullable=False, unique=True)
    id_branch = Column(String(length=100), nullable=True )
    id_product = Column(Integer, ForeignKey('branch.id'), nullable=False)
    Rbranch = relationship("Branch", back_populates="Rproductxpart")
    Rsupplier = relationship("supplier", back_populates="Rproductxpart")
    Rproduct = relationship("product", back_populates="Rproductxspart")
