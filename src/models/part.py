from sqlalchemy import Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from src.config.database import Base

class Part(Base):
    __tablename__ = 'part'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=100), nullable=False, unique=True)
    quantity = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)
    id_branch = Column(Integer, ForeignKey('branch.id'), nullable=False)
    Rbranch = relationship("Branch", back_populates="Rpart")
    Rsupplierxpart = relationship("Supplierxpart", back_populates="Rpart")

