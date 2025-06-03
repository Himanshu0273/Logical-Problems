from fastapi import APIRouter, Depends, status, HTTPException
from typing import List
from sqlalchemy.orm import Session
from .. import schemas, database, models, oauth2

router = APIRouter(
    prefix="/blog",
    tags=['Blogs']
)
get_db = database.get_db
#Get all blogs from DB
@router.get('/', status_code=200,response_model=List[schemas.ShowBlog])
def get_all_blogs(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    blogs = db.query(models.Blog).all()
    return blogs

#Create new blogs
@router.post("/", status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    new_blog = models.Blog(title=request.title, body=request.body, author_id = 1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog  


#Get the blog according to id
@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
def get_required_blog(id, db: Session=Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} is not available.")
    return blog


#Update a Blog
@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_blog(id: int, request: schemas.Blog, db: Session=Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    print(blog)
    if not blog:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} is not available.")

    blog.update(request.dict()  )
    db.commit()
    return 'Blog Updated!!'

#Delete a Blog
@router.delete('/{id}')
def delete_blog(id, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} is not available.")
    blog.delete(synchronize_session=False)
    db.commit()
    return 'Blog Deleted!!'

