from app.routes.crud_router import make_crud_router
from app.models import Payment
from app.schemas import PaymentIn, PaymentOut

router = make_crud_router(Payment, PaymentIn, PaymentOut)