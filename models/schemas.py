from pydantic import BaseModel


class PostBase(BaseModel):
    title: str
    post_text: str
    author: str

    class Config:
        orm_mode = True


class PostList(PostBase):
    id: int


class PostCreate(PostBase):
    pass
