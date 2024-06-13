from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

outh2_scheme = OAuth2PasswordBearer(tokenUrl='login')

def get_current_user(token : str = Depends(outh2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"www.authenticate":"bearer"}
        )
    

