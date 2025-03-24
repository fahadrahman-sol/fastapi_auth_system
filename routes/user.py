from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from schemas import UserCreate
from crud import create_user, get_user, update_user, delete_user

router = APIRouter()

@router.post("/create")
def create(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)

@router.get("/read/{user_id}")
def read(user_id: str, db: Session = Depends(get_db)):
    user = get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/update/{user_id}")
def update(user_id: str, user_data: UserCreate, db: Session = Depends(get_db)):
    updated_user = update_user(db, user_id, user_data)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User updated"}

@router.delete("/delete/{user_id}")
def delete(user_id: str, db: Session = Depends(get_db)):
    if not delete_user(db, user_id):
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted"}
