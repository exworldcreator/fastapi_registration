from fastapi import APIRouter, FastAPI, Depends, HTTPException, Request
import models, crud, schemas
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from fastapi.responses import HTMLResponse

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@router.get("/")
def main():
    return {"message": "Hello World!"}

@router.post("/register/", response_model=schemas.UserResponse)
async def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)