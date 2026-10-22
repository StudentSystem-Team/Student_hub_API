
from sqlalchemy.orm import Session
from app import models, schemas


def create_student(db: Session, student: schemas.StudentCreate):
    new_student = models.Student(
        name=student.name,
        age=student.age,
        email=str(student.email),
        course=student.course,
    )
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student


def get_all_students(db: Session):
    return db.query(models.Student).order_by(models.Student.id).all()


def get_student_by_id(db: Session, student_id: int):
    return (
        db.query(models.Student)
        .filter(models.Student.id == student_id)
        .first()
    )


def update_student(
    db: Session,
    student_id: int,
    student_data: schemas.StudentUpdate,
):
    student = get_student_by_id(db, student_id)

    if student is None:
        return None

    student.name = student_data.name
    student.age = student_data.age
    student.email = str(student_data.email)
    student.course = student_data.course

    db.commit()
    db.refresh(student)
    return student


def delete_student(db: Session, student_id: int):
    student = get_student_by_id(db, student_id)

    if student is None:
        return None

    db.delete(student)
    db.commit()
    return student
