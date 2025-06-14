from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from db.session import get_db
from schemas.blog import CreateBlog, ShowBlog, UpdateBlog
from db.repository.blog import create_new_blog,retreive_blog, list_blogs,update_blog_by_id
from typing import List

router = APIRouter()
@router.post("/", response_model=ShowBlog, status_code=status.HTTP_201_CREATED)
def create_blog(blog: CreateBlog, db: Session = Depends(get_db)):
    """
    Create a new blog
    """
    blog = create_new_blog(blog=blog, db=db,author_id=1)
    return ShowBlog(
        title=blog.title,
        content=blog.content,
        created_at=blog.created_at
    )

@router.get("/{id}", response_model=ShowBlog)
def get_blog(id:int, db:Session = Depends(get_db)):
    blog = retreive_blog(id=id, db=db)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with {id} not found")
    return blog

@router.get("", response_model=List[ShowBlog])
def get_all_blogs(db:Session = Depends(get_db)):
    blogs = list_blogs(db=db)
    return blogs

@router.put("/{id}", response_model=ShowBlog)
def update_blog(id:int, blog:UpdateBlog, db:Session = Depends(get_db)):
    blog = update_blog_by_id(id=id, db=db,blog=blog, author_id=1)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with {id} not found")
    return blog