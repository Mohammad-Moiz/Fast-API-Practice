from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session
from Blog import schemas, models
from Blog.database import get_db

router = APIRouter(tags=['Blogs'])
                #    ,prefix="/blog"


@router.get('/blog', response_model=list[schemas.ShowBlog])
def all(db:Session=Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs


@router.post('/blog', status_code=status.HTTP_201_CREATED)
def create_blog(request : schemas.Blog, db:Session=Depends(get_db)):
    new_blog = models.Blog(title=request.title, body=request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@router.delete('/blog/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db:Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"blog with the id {id} is not found.")
    blog.delete(synchronize_session=False)
    db.commit()
    return "done!"

@router.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED)
def updated(id, requests = schemas.Blog, db:Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).update(requests)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"blog with the id {id} is not found.")
    blog.update(requests)
    db.commit()
    return "updated successfully!"

@router.get('/blog/{id}', status_code=200, response_model=schemas.ShowBlog)
def show(id,response=Response, db:Session=Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"blog with the id {id} is not available.")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'Detail' : f"blog with the id {id} is not available."}
    else:
        return blog

