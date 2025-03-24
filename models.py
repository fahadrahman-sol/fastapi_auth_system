from sqlalchemy import Column, String, DateTime
from database import Base
from datetime import datetime
import uuid

def generate_uuid():
    return str(uuid.uuid4())[:16]

class User(Base):
    __tablename__ = "users"

    id = Column(String(16), primary_key=True, default=generate_uuid)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)  # Hashed password
    role = Column(String, default="candidates")
    created_on = Column(DateTime, default=datetime.utcnow)
    modified_on = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
