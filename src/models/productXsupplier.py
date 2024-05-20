from sqlalchemy import Column, String, Integer,ForeignKey ,Boolean
from sqlalchemy.orm import relationship
from src.config.database import Base

class Productxsupplier(Base):
    __tablename__ = 'productxsupplier'
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_supplier = Column(Integer,ForeignKey('supplier.id') ,nullable=False, unique=True)
    id_branch = Column(Integer,ForeignKey('branch.id'), nullable=True )
    id_product = Column(Integer, ForeignKey('product.id'), nullable=False)
    Rbranch = relationship("Branch", back_populates="Rproductxsupplier")
    Rsupplier = relationship("Supplier", back_populates="Rproductxsupplier")
    Rproduct = relationship("Product", back_populates="Rproductxsupplier")
