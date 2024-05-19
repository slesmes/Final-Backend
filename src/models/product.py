from sqlalchemy import Column, String, Integer,ForeignKey ,Boolean
from sqlalchemy.orm import relationship
from src.config.database import Base

class Product(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=100), nullable=False, unique=True)
    price = Column(Integer, nullable=False )
    quantity = Column(Integer, nullable=False )
    description = Column(String(length=100),nullable=False )
    status = Column(Boolean, nullable=False, default=True)
    disccount= Column(float,nullable=True)
    id_category = Column(Integer, ForeignKey('category.id'), nullable=False)
    id_branch = Column(Integer, ForeignKey('branch.id'), nullable=False)
    Rcategory = relationship("Category", back_populates="Rproduct")
    Rbranch = relationship("Branch", back_populates="Rproduct")
    Rproductxsupplier = relationship("Productxsupplier", back_populates="Rproduct")
    Rproductxpart = relationship("Productxpart", back_populates="Rproduct")
