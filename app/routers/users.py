from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas
from app.database import get_db
from app import utils, models
from .. import oauth2

router = APIRouter(prefix="/users", tags=["Users"])


# ROUTE FOR CREATING A USER
@router.post(
    "/",
    response_model=schemas.UserCreationOut,
    status_code=status.HTTP_201_CREATED,
)
def create_user(user: schemas.UserCreation, db: Session = Depends(get_db)):
    # Check if the user is already registered in the database
    user_in_db = db.query(models.User).filter(models.User.email == user.email).first()
    if user_in_db:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"your email is already registered",
        )

    # Hash user's password
    user.password = utils.get_password_hash(user.password)

    new_user = models.User(email=user.email, password=user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


# ROUTE FOR DELETING A USER
@router.delete("/{id}")
def delete_user(
    id: int,
    db: Session = Depends(get_db),
    current_user: int = Depends(oauth2.get_current_user),
):
    # Check if the user with the specified ID exists in the database.
    user_query = db.query(models.User).filter(models.User.id == id)
    user = user_query.first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID {id}, was not found",
        )

    # Ensure the current user is the owner of the account they are trying to delete.
    if current_user.id != user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f"You are not allowed to delete someone's else account",
        )

    # Perform the deletion using the query object for efficiency.
    user_query.delete(synchronize_session=False)
    db.commit()

    return {"message": f"successfully deleted user with ID {id}"}


# ROUTE FOR GETTING A USER BY ID
@router.get("/{id}", response_model=schemas.UserInfoOut)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    # If user is not found
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID {id}, was not found",
        )

    return user
