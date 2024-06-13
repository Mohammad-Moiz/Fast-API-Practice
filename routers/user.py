from fastapi import APIRouter, Depends, status, HTTPException
from Blog import hashing, main, schemas, models
from sqlalchemy.orm import Session
from Blog.database import get_db

router = APIRouter(tags=['Users'])


@router.post('/user', response_model=schemas.User)
def create_user(requests:schemas.User, db:Session = Depends(get_db)):
    new_user = models.User(name=requests.name, email=requests.email, password=hashing.Hash.bcrypt(requests.password))
    db.add(new_user)
    db.commit()
    db.refresh()
    return new_user


@router.get('/user/{id}', response_model=schemas.User)
def get_user(id:int, db:Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"blog with the id {id} is not found.")
    return user
