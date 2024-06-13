from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from Blog import schemas, models
from Blog.database import LocalSession
from Blog.hashing import Hash
from datetime import timedelta
from routers.token import create_access_token


router = APIRouter(tags=['Authentication'])

ACCESS_TOKEN_EXPIRE_MINUTES = 30

def get_db():
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()

@router.post('/login')
def login(request=schemas.Login, db:Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.username)

    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentials.")
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Incorrect Password.")
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={'sub':user.username}, expires_delta=access_token_expires)
    
    return {'acess_token':access_token, 'token_type': 'bearer'}