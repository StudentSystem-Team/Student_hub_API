from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.dependencies import get_current_user, require_roles


def make_crud_router(Model, In, Out, writers=("teacher", "admin")):
    router = APIRouter()
    writer = require_roles(*writers)

    @router.get("/", response_model=list[Out])
    def list_all(db: Session = Depends(get_db), user=Depends(get_current_user)):
        return db.query(Model).all()

    @router.post("/", response_model=Out)
    def create(data: In, db: Session = Depends(get_db), user=Depends(writer)):
        obj = Model(**data.model_dump())
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj

    @router.put("/{id}", response_model=Out)
    def update(id: int, data: In, db: Session = Depends(get_db), user=Depends(writer)):
        obj = db.get(Model, id)
        if not obj:
            raise HTTPException(404, "Not found")
        for k, v in data.model_dump().items():
            setattr(obj, k, v)
        db.commit()
        db.refresh(obj)
        return obj

    @router.delete("/{id}")
    def delete(id: int, db: Session = Depends(get_db), user=Depends(writer)):
        obj = db.get(Model, id)
        if not obj:
            raise HTTPException(404, "Not found")
        db.delete(obj)
        db.commit()
        return {"message": "Deleted"}

    return router