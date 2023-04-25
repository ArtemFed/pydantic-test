from sqlalchemy import Column, String, Integer
from repo.db import *


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(String(30))
    author = Column(String(30))
    post_text = Column(String)
