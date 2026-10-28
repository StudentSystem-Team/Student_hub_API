from app.routes.crud_router import make_crud_router
from app.models import Fee
from app.schemas import FeeIn, FeeOut

router = make_crud_router(Fee, FeeIn, FeeOut)