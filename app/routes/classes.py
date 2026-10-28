from app.routes.crud_router import make_crud_router
from app.models import SchoolClass
from app.schemas import ClassIn, ClassOut

router = make_crud_router(SchoolClass, ClassIn, ClassOut)