from app.routes.crud_router import make_crud_router
from app.models import Mark
from app.schemas import MarkIn, MarkOut

router = make_crud_router(Mark, MarkIn, MarkOut)