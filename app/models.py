from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(String(16), primary_key=True, index=True)
    first_name = Column(String(100), index=True)
    last_name = Column(String(100), index=True)
    email = Column(String(255), unique=True, index=True)
    password = Column(String(255))
    role = Column(String(50), default="candidates")
    created_on = Column(TIMESTAMP, default=func.now())
    modified_on = Column(TIMESTAMP, default=func.now(), onupdate=func.now())
