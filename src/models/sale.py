from sqlalchemy import Column, String, Integer,ForeignKey ,Boolean
from sqlalchemy.orm import relationship
from src.config.database import Base

class Sale(Base):
    __tablename__ = 'sale'
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_product = Column(Integer, ForeignKey('product.id'),nullable=False)
    id_bill = Column(Integer, ForeignKey('bill.id'),nullable=False )
    id_branch = Column(Integer, ForeignKey('branch.id'),nullable=False )
    quantity = Column(Integer, nullable=False)
    Rproduct = relationship("Product", back_populates="Rsale")
    Rbill = relationship("Bill", back_populates="Rsale")
    Rbranch = relationship("Branch", back_populates="Rsale")


