from app.routes.crud_router import make_crud_router
from app.models import Result
from app.schemas import ResultIn, ResultOut

router = make_crud_router(Result, ResultIn, ResultOut)