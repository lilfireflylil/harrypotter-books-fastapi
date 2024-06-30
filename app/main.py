from fastapi import FastAPI
from .routers import add_books_in_db, users, auth, books
from .database import engine
from . import models


models.Base.metadata.create_all(bind=engine)


app = FastAPI()
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(books.router)
app.include_router(add_books_in_db.router)


@app.get("/")
def home():
    return {
        "base_url": "http://127.0.0.1:8000/",
        "to add books data in database": "GET // http://127.0.0.1:8000/add_books",
        "showing all books": "GET // http://127.0.0.1:8000/books",
        "showing single book details by ID": "GET // http://127.0.0.1:8000/books/{ID}",
        "create an account": "POST // http://127.0.0.1:8000/users",
        "showing an account details by ID": "GET // http://127.0.0.1:8000/users/{ID}",
        "login to account": "POST // http://127.0.0.1:8000/login/",
        # Login credential must be typed in form fields, not json
        "delete an account by ID": "DELETE // http://127.0.0.1:8000/users/{ID}",
        "for better documentations, visit": "http://127.0.0.1:8000/docs",
    }
