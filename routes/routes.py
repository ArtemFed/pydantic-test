from fastapi import APIRouter
from handlers import posts

routes = APIRouter()

routes.include_router(posts.router, prefix="/blog")
