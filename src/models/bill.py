from sqlalchemy import Column, String, Integer,ForeignKey ,Boolean
from sqlalchemy.orm import relationship
from src.config.database import Base

class Bill(Base):
    __tablename__ = 'bill'
    id = Column(Integer, primary_key=True, autoincrement=True)
    date_bill = Column(String(length=100), nullable=False)
    status = Column(Boolean,nullable=False, default=True )
    id_client = Column(String(length=100), ForeignKey('client.identification'), nullable=False )
    id_user = Column(String(length=100), ForeignKey('user.identification'), nullable=False )
    id_branch = Column(Integer, ForeignKey('branch.id'), nullable=False )
    Rclient = relationship("Client", back_populates="Rbill")
    Rbranch = relationship("Branch", back_populates="Rbill")
    Ruser = relationship("User", back_populates="Rbill")
    Rsale = relationship("Sale", back_populates="Rbill")

