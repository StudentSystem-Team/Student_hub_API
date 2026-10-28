from app.routes.crud_router import make_crud_router
from app.models import Attendance
from app.schemas import AttendanceIn, AttendanceOut

router = make_crud_router(Attendance, AttendanceIn, AttendanceOut)