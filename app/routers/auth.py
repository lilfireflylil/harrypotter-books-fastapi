from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import database, schemas, models, utils, oauth2
from fastapi.security.oauth2 import OAuth2PasswordRequestForm, OAuth2PasswordBearer

router = APIRouter(prefix="/login", tags=["Authentication"])


@router.post("/")
def login(
    user_credentials: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(database.get_db),
):
    # Check if the user is already registered in the database.
    user_in_db = (
        db.query(models.User)
        .filter(models.User.email == user_credentials.username)
        .first()
    )

    if not user_in_db:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials"
        )

    # User's attempted password must be hashed and compared with hashed password in the database.
    # The below function will do it all and returns boolean value.
    match_password = utils.verify_password(
        user_credentials.password, user_in_db.password
    )
    if not match_password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials"
        )

    data = {"user_id": user_in_db.id}
    access_token = oauth2.create_access_token(data)

    return {"access_token": access_token, "token_type": "bearer"}
