from app.routes.crud_router import make_crud_router
from app.models import Examination
from app.schemas import ExamIn, ExamOut

router = make_crud_router(Examination, ExamIn, ExamOut)