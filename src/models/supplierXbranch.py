from sqlalchemy import Column, String, Integer,ForeignKey ,Boolean
from sqlalchemy.orm import relationship
from src.config.database import Base

class Supplierxbranch(Base):
    __tablename__ = 'supplierxbranch'
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_supplier = Column(Integer,ForeignKey('supplier.id') ,nullable=False)
    id_branch = Column(String(length=100), nullable=False )
    Rsupplier = relationship("Supplier", back_populates="Rsupplierxbranch")
    Rbranch = relationship("Branch", back_populates="Rsupplierxbranch")

