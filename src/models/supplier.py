from sqlalchemy import Column, String, Integer,ForeignKey ,Boolean
from sqlalchemy.orm import relationship
from src.config.database import Base

class Supplier(Base):
    __tablename__ = 'supplier'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=100), nullable=False, unique=True)
    name_seller = Column(String(length=100), nullable=False )
    status = Column(Boolean, nullable=False, default=True)
    phone = Column(String(length=100), nullable=False )
    Rsupplierxbranch = relationship("Supplierxbranch",back_populates="Rsupplier")
    Rsupplierxpart = relationship("Supplierxpart",back_populates="Rsupplier")
    Rproductxsupplier = relationship("Productxsupplier",back_populates="Rsupplier")
    Rproductxpart = relationship("Productxpart",back_populates="Rsupplier")

