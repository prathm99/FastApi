from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from db.session import get_db
from schemas.blog import CreateBlog, ShowBlog
from db.repository.blog import create_new_blog,retreive_blog


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

@router.get("/{id}", response_model=ShowBlog )
def get_blog(id:int, db:Session = Depends(get_db)):
    blog = retreive_blog(id=id, db=db)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with {id} not found")
    return blog