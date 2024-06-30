from jose import jwt, JWTError
from .config import settings
from datetime import datetime, timedelta, timezone
from . import schemas, database, models
from fastapi.security.oauth2 import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc).astimezone() + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )
    to_encode.update({"exp": expire})

    access_token = jwt.encode(to_encode, SECRET_KEY, ALGORITHM)

    return access_token


def verify_access_token(token: str, credentials_exception, db: Session):
    try:
        payload = jwt.decode(token, SECRET_KEY, ALGORITHM)
        id = payload.get("user_id")

        if id is None:
            raise credentials_exception

        token_data = schemas.TokenData(id=id)

        # Query the database to check if the user exists.
        # Ensures that a user who has been deleted but still has a valid
        # token cannot perform operations.
        user_in_db = (
            db.query(models.User).filter(models.User.id == token_data.id).first()
        )
        if user_in_db is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="The user associated with current access token could not be found or has been deleted. Please register again",
                headers={"WWW-Authenticate": "Bearer"},
            )

    except JWTError:
        # Raise the credentials exception if there is any issue with decoding the token.
        raise credentials_exception

    return token_data


oauth2_schema = OAuth2PasswordBearer(tokenUrl="login")


def get_current_user(
    token: str = Depends(oauth2_schema), db: Session = Depends(database.get_db)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    return verify_access_token(token, credentials_exception, db)
