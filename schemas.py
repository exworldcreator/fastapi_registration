from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str
    password: str
    
    class Config:
        from_attributes = True

class UserResponse(BaseModel):
    id: int
    email: str
    
    class Config:
        from_attributes = True