from app.routes.crud_router import make_crud_router
from app.models import Teacher
from app.schemas import TeacherIn, TeacherOut

router = make_crud_router(Teacher, TeacherIn, TeacherOut)