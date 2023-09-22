from typing import Optional

from pydantic import BaseModel, EmailStr, constr
from datetime import datetime
from db.models import Role
from uuid import UUID


class TunedModel(BaseModel):
    class Config:
        orm_mode = True
    

class ShowUser(TunedModel):
    id: UUID
    first_name: str
    second_name: str
    email: EmailStr
    birth_date: datetime
    is_disabled: bool
    

class CreateUser(BaseModel):
    first_name: str
    second_name: str
    email: EmailStr
    password: str
    birth_date: datetime
    
    
class UpdateUserRequest(BaseModel):
    first_name: Optional[constr(min_length=1)]
    second_name: Optional[constr(min_length=1)]
    email: Optional[EmailStr]
    birth_date: Optional[datetime]
    
    
class UpdateUserResponse(BaseModel):
    id: UUID
    

class DeleteUserResponse(BaseModel):
    id: UUID