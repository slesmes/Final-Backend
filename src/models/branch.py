from sqlalchemy import Column, String, Integer,ForeignKey ,Boolean
from sqlalchemy.orm import relationship
from src.config.database import Base

class Branch(Base):
    __tablename__ = 'branch'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=100), nullable=False, unique=True)
    id_city = Column(Integer,ForeignKey('city.id') ,nullable=False )
    id_company = Column(Integer, ForeignKey('company.id'), nullable=False )
    address = Column(String(length=100),nullable=False )
    phone = Column(String(length=100), nullable=False)
    status= Column(Boolean,nullable=False, default=True)
    Rcity = relationship("City", back_populates="Rbranch")
    Rcompany = relationship("Company", back_populates="Rbranch")
    Rrol = relationship("Rol", back_populates="Rbranch")
    Ruser = relationship("User", back_populates="Rbranch")
    Rsupplierxbranch = relationship("Supplierxbranch", back_populates="Rbranch")
    Rpart = relationship("Part", back_populates="Rbranch")
    Rsupplierxpart = relationship("Supplierxpart", back_populates="Rbranch")
    Rbill = relationship("Bill", back_populates="Rbranch")
    Rproduct = relationship("Product", back_populates="Rbranch")
    Rproductxsupplier = relationship("Productxsupplier", back_populates="Rbranch")
    Rproductxpart = relationship("Productxpart", back_populates="Rbranch")
    Rcategory = relationship("Category", back_populates="Rbranch")


