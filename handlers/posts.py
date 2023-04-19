from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from handlers import service
from models.schemas import PostCreate, PostList
from starlette.requests import Request

router = APIRouter()


def get_db(request: Request):
    return request.state.db


@router.get("/", response_model=List[PostList])
def post_list(db: Session = Depends(get_db)):
    return service.get_post_list(db)


@router.post("/")
def post_list(item: PostCreate, db: Session = Depends(get_db)):
    return service.create_post(db, item)
