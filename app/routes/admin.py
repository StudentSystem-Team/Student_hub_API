from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.dependencies import require_roles
from app.services.dashboard import get_dashboard_summary


router = APIRouter(prefix="/admin", tags=["Admin"])


@router.get("/dashboard")
def get_admin_dashboard(
    db: Session = Depends(get_db),
    user=Depends(require_roles("admin"))
):
    return get_dashboard_summary(db)