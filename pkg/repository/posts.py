from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pkg.core.utils import get_db
from pkg.service import service
from models.schemas import PostCreate

router = APIRouter()


@router.get("/")
def post_list(db: Session = Depends(get_db)):
    return service.get_post_list(db)


@router.post("/")
def post_list(item: PostCreate, db: Session = Depends(get_db)):
    return service.create_post(db, item)
