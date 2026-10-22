
from pydantic import BaseModel, ConfigDict, EmailStr, Field


class StudentCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    age: int = Field(ge=1, le=120)
    email: EmailStr
    course: str = Field(min_length=2, max_length=100)


class StudentUpdate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    age: int = Field(ge=1, le=120)
    email: EmailStr
    course: str = Field(min_length=2, max_length=100)


class StudentResponse(BaseModel):
    id: int
    name: str
    age: int
    email: EmailStr
    course: str

    model_config = ConfigDict(from_attributes=True)
