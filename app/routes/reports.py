from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.dependencies import get_current_user
from app import models

router = APIRouter()


@router.get("/")
def get_report(db: Session = Depends(get_db), user=Depends(get_current_user)):
    fees = db.query(models.Fee).all()
    marks = db.query(models.Mark).all()
    attendance = db.query(models.Attendance).all()

    present = sum(1 for a in attendance if (a.status or "").lower() == "present")
    avg_marks = round(sum((m.marks or 0) for m in marks) / len(marks), 1) if marks else 0

    return {
        "total_students": db.query(models.Student).count(),
        "total_teachers": db.query(models.Teacher).count(),
        "total_classes": db.query(models.SchoolClass).count(),
        "total_subjects": db.query(models.Subject).count(),
        "total_exams": db.query(models.Examination).count(),
        "attendance_records": len(attendance),
        "attendance_present": present,
        "average_marks": avg_marks,
        "fees_collected": sum((f.amount or 0) for f in fees if (f.status or "").lower() == "paid"),
        "fees_pending": sum((f.amount or 0) for f in fees if (f.status or "").lower() != "paid"),
    }