
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app import models
from app.auth_utils import decode_access_token
from app.database import get_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
):
    payload = decode_access_token(token)

    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired login token.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    username = payload.get("sub")

    if not username:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid login token.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    user = (
        db.query(models.User)
        .filter(models.User.username == username)
        .first()
    )

    if not user or payload.get("role") != user.role:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User account is invalid. Please log in again.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user


def require_roles(*allowed_roles: str):
    def role_checker(
        current_user=Depends(get_current_user),
    ):
        if current_user.role.lower() not in [
            role.lower() for role in allowed_roles
        ]:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You do not have permission to access this resource.",
            )

        return current_user

    return role_checker
