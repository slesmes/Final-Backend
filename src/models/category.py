from sqlalchemy import Column, String, Integer,ForeignKey ,Boolean
from sqlalchemy.orm import relationship
from src.config.database import Base

class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=100), nullable=False, unique=True)
    description = Column(String(length=100), nullable=True )
    id_category = Column(Integer, ForeignKey('category.id'), nullable=False)
    Rbranch = relationship("Branch", back_populates="Rcategory")
    Rproduct = relationship("Product", back_populates="Rcategory")


