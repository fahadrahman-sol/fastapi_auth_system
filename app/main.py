from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, database
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

app = FastAPI()

# Dependency to get the DB session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/", response_model=schemas.UserResponse)
async def create_user(user: schemas.UserCreate, db: AsyncSession = Depends(get_db)):
    # Check if email already exists
    result = await db.execute(select(models.User).filter(models.User.email == user.email))
    existing_user = result.scalars().first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Create a new user record
    db_user = models.User(**user.dict())
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)  # Get the newly added user with auto-generated fields

    return db_user
