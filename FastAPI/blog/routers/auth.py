from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import schemas, database, models, schemas
from ..hashing import Hash
from ..token import create_access_token
from fastapi.security import OAuth2PasswordRequestForm

get_db = database.get_db

router = APIRouter(
    tags=['Auth']
)

@router.post('/login')
def login(request: OAuth2PasswordRequestForm=Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == request.username).first()
    if not user:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentials.")
        
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f"Incorrect Password.")
        
    #Generate JWT Token
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}