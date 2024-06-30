from .database import Base
from sqlalchemy import Column, Integer, String, TIMESTAMP, func, Date, Text


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    created_at = Column(
        TIMESTAMP(timezone=True), server_default=func.now(), nullable=False
    )

    def __str__(self):
        return f"{self.id=} {self.email=} {self.created_at=}"


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    book_id = Column(String, index=True)
    title = Column(String, index=True)
    author = Column(String)
    cover = Column(String)
    release_date = Column(Date)
    total_chapters = Column(Integer)
    pages = Column(Integer)
    summary = Column(Text)
    wiki = Column(String)

    def __str__(self):
        return f"Book's {self.id=}, {self.title=} {self.author=} {self.release_date=}"
