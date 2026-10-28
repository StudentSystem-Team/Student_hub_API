from fastapi import APIRouter
router = APIRouter(prefix="/api/portal", tags=["Portal"])
@router.get("/teacher-dashboard")
def teacher_dashboard(): return {"students": 120, "teachers": 15, "classes": 6, "subjects": 10}
@router.get("/student-dashboard")
def student_dashboard(): return {"attendance": 85, "subjects": 5, "assignments": 3}