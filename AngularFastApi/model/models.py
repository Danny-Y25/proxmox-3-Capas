from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True)
    firstname = Column(String, unique=False, index=True)
    lastname = Column(String, unique=False, index=True)
    username = Column(String, unique=True, index=True)
    country = Column(String, unique=False, index=True)
    password_user = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner") 
