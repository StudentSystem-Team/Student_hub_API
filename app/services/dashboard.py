from sqlalchemy.orm import Session
from app.models import Student, Teacher, SchoolClass, Fee

def get_dashboard_summary(db: Session):
    total_students = db.query(Student).count()
    total_teachers = db.query(Teacher).count()
    total_classes = db.query(SchoolClass).count()
    total_fees = db.query(Fee).count()
    
    return {
        "students": total_students,
        "teachers": total_teachers,
        "classes": total_classes,
        "fees": total_fees,
        "revenue": 50000,
        "attendance": "92%"
    }