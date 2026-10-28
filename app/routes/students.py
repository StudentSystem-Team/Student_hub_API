from app.routes.crud_router import make_crud_router
from app.models import Student
from app.schemas import StudentIn, StudentOut

router = make_crud_router(Student, StudentIn, StudentOut, writers=("teacher", "admin", "student"))