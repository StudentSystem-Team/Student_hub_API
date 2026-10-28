from app.routes.crud_router import make_crud_router
from app.models import Assignment
from app.schemas import AssignmentIn, AssignmentOut

router = make_crud_router(Assignment, AssignmentIn, AssignmentOut)