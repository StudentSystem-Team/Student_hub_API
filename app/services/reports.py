from sqlalchemy.orm import Session
from app.models import Attendance, Fee, Result

def attendance_report(db: Session):
    try:
        data = db.query(Attendance).all()
        return {"total": len(data), "data": data}
    except:
        return {"total": 0, "data": []}

def fee_report(db: Session):
    try:
        data = db.query(Fee).all()
        return {"total": len(data), "data": data}
    except:
        return {"total": 0, "data": []}

def result_report(db: Session):
    try:
        data = db.query(Result).all()
        return {"total": len(data), "data": data}
    except:
        return {"total": 0, "data": []}

def exam_result_report(db: Session):
    return result_report(db)

def get_reports_summary(db: Session):
    return {
        "attendance": attendance_report(db),
        "fees": fee_report(db),
        "results": result_report(db)
    }

# Aliases for any name
exam_report = result_report
attendance_reports = attendance_report
fee_reports = fee_report