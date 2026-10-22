
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel, EmailStr, Field

from app.database import get_db
from app.models import Student

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)


# Pydantic model for creating a student
class StudentCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    age: int = Field(gt=0)
    email: EmailStr
    course: str = Field(min_length=1, max_length=100)


# Pydantic model for updating a student
class StudentUpdate(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    age: int = Field(gt=0)
    email: EmailStr
    course: str = Field(min_length=1, max_length=100)


# CREATE: Add a student
@router.post("/", status_code=201)
def create_student(
    student: StudentCreate,
    db: Session = Depends(get_db)
):
    existing = db.query(Student).filter(
        Student.email == student.email
    ).first()

    if existing:
        raise HTTPException(
            status_code=409,
            detail="Email already exists"
        )

    new_student = Student(
        name=student.name,
        age=student.age,
        email=student.email,
        course=student.course
    )

    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return new_student


# READ: Get all students
@router.get("/")
def get_students(db: Session = Depends(get_db)):
    return db.query(Student).all()


# READ: Get one student by ID
@router.get("/{student_id}")
def get_student(
    student_id: int,
    db: Session = Depends(get_db)
):
    student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student


# UPDATE: Update a student
@router.put("/{student_id}")
def update_student(
    student_id: int,
    updated_data: StudentUpdate,
    db: Session = Depends(get_db)
):
    student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    duplicate_email = db.query(Student).filter(
        Student.email == updated_data.email,
        Student.id != student_id
    ).first()

    if duplicate_email:
        raise HTTPException(
            status_code=409,
            detail="Email already belongs to another student"
        )

    student.name = updated_data.name
    student.age = updated_data.age
    student.email = updated_data.email
    student.course = updated_data.course

    db.commit()
    db.refresh(student)

    return student


# DELETE: Delete a student
@router.delete("/{student_id}")
def delete_student(
    student_id: int,
    db: Session = Depends(get_db)
):
    student = db.query(Student).filter(
        Student.id == student_id
    ).first()

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    db.delete(student)
    db.commit()

    return {
        "message": "Student deleted successfully"
    }