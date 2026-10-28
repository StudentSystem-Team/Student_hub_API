from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import models, schemas
from app.auth_utils import (
    hash_password,
    verify_password,
    create_access_token,
)
from app.database import get_db
from app.dependencies import get_current_user

router = APIRouter()


@router.post("/register", status_code=status.HTTP_201_CREATED)
def register(
    user: schemas.UserCreate,
    db: Session = Depends(get_db),
):
    username = user.username.strip().lower()
    role = user.role.strip().lower()

    if not username:
        raise HTTPException(
            status_code=400,
            detail="Email address is required.",
        )

    if len(user.password) < 8:
        raise HTTPException(
            status_code=400,
            detail="Password must contain at least 8 characters.",
        )

    if role not in ("student", "teacher"):
        raise HTTPException(
            status_code=403,
            detail="Only student and teacher registration is allowed.",
        )

    existing_user = (
        db.query(models.User)
        .filter(models.User.username == username)
        .first()
    )

    if existing_user:
        raise HTTPException(
            status_code=409,
            detail="This email is already registered. Please log in.",
        )

    new_user = models.User(
        username=username,
        password=hash_password(user.password),
        role=role,
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    # Create the matching profile record so the profile page has details
    display_name = (user.name or "").strip() or username
    if role == "student":
        db.add(models.Student(name=display_name, email=username, class_name=""))
    else:
        db.add(models.Teacher(name=display_name, email=username, subject=""))
    db.commit()

    return {
        "message": "Registration successful. Please log in.",
        "username": new_user.username,
        "role": new_user.role,
    }


@router.post("/login")
def login(
    user: schemas.UserLogin,
    db: Session = Depends(get_db),
):
    username = user.username.strip().lower()

    db_user = (
        db.query(models.User)
        .filter(models.User.username == username)
        .first()
    )

    if not db_user or not verify_password(
        user.password,
        db_user.password,
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    if db_user.role not in ("student", "teacher", "admin"):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="This account has an invalid role.",
        )

    access_token = create_access_token(
        subject=db_user.username,
        role=db_user.role,
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "role": db_user.role,
    }


@router.get("/me")
def get_me(
    current_user=Depends(get_current_user),
):
    return {
        "id": current_user.id,
        "username": current_user.username,
        "role": current_user.role,
    }