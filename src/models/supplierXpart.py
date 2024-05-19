from sqlalchemy import Column, String, Integer,ForeignKey ,Boolean
from sqlalchemy.orm import relationship
from src.config.database import Base

class Supplierxpart(Base):
    __tablename__ = 'supplierxpart'
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_part= Column(Integer, ForeignKey('part'), nullable=False)
    id_supplier = Column(Integer, ForeignKey('supplier'), nullable=False)
    id_branch = Column(Integer, ForeignKey('branch'), nullable=False)
    Rpart = relationship("Part", back_populates="Rsupplierxpart")
    Rsupplier = relationship("Supplier", back_populates="Rsupplierxpart")
    Rbranch = relationship("Branch", back_populates="Rsupplierxpart")

