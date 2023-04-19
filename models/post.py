from sqlalchemy import Column, String, Integer
from pkg.core.db import Base


class Post(Base):
    __tablename__ = "repository"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(String(30))
    author = Column(String(30))
    post_text = Column(String)
