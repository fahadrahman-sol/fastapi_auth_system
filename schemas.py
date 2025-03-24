from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str
    role: str = "candidates"

class LoginRequest(BaseModel):
    email: EmailStr
    password: str
