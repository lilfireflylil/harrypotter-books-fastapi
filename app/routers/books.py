from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models, schemas
from typing import List


router = APIRouter(prefix="/books", tags=["Books"])


# ROUTE FOR GETTING ALL THE BOOKS
@router.get("/", response_model=List[schemas.Books])
def get_books(db: Session = Depends(get_db)):
    books = db.query(models.Book).all()
    if not books:
        raise HTTPException(status.HTTP_200_OK, f"no book")
    return books


# ROUTE FOR GETTING A SINGLE BOOK
@router.get("/{id}", response_model=schemas.Book)
def get_book(id: int, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == id).first()
    if not book:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND, f"Book with ID {id} was not found"
        )

    return book
