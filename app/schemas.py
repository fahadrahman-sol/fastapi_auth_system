from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    id: str
    first_name: str
    last_name: str
    email: str
    password: str
    role: Optional[str] = "candidates"  # Default role is candidates

    class Config:
        orm_mode = True

class UserResponse(UserCreate):
    created_on: str
    modified_on: str
