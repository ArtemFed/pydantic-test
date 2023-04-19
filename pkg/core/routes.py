from fastapi import APIRouter
from pkg.repository import posts

routes = APIRouter()

routes.include_router(posts.router, prefix="/blog")
