from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.future import select

DATABASE_URL = "postgresql+asyncpg://postgres:1234@localhost/sol_resume_chat"

engine = create_engine(DATABASE_URL, echo=True, future=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=sessionmaker.asyncio.AsyncSession)

Base = declarative_base()
