from typing import Optional
from pydantic import BaseModel, model_validator
from datetime import datetime

class CreateBlog(BaseModel):
    title: str
    slug: str
    content: Optional[str] = None
    author_id: int

    @model_validator(mode='before')
    def generate_slug(cls, values):
        title = values.get('title')
        if title:
            values['slug'] = title.replace(" ", "-").lower()
        return values

class UpdateBlog(CreateBlog):
    pass


class ShowBlog(BaseModel):
    title: str
    content: Optional[str] = None
    created_at: datetime

    class Config():
        orm_mode=True
