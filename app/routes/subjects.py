from app.routes.crud_router import make_crud_router
from app.models import Subject
from app.schemas import SubjectIn, SubjectOut

router = make_crud_router(Subject, SubjectIn, SubjectOut)