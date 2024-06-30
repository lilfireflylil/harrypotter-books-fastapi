from pydantic import (
    BaseModel,
    ConfigDict,
    EmailStr,
    Field,
    field_validator,
    AwareDatetime,
)
from datetime import datetime, date
from typing import Optional, Any


class UserCreation(BaseModel):
    # Ensure no extra fields are accepted
    model_config = ConfigDict(extra="forbid")

    email: EmailStr

    # Descriptive message is useful for generating API documentation.
    password: str = Field(
        min_length=4,
        description="Password length must be greater than 3 characters",
    )

    # Custom validator to convert email to lower-case
    @field_validator("email")
    @classmethod
    def lower_case_email(cls, value: str) -> str:
        return value.lower()


class UserCreationOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    email: EmailStr
    created_at: datetime


class UserInfoOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    email: EmailStr
    created_at: AwareDatetime

    # Custom validator to strip the timezone from the created_at field
    @field_validator("created_at")
    @classmethod
    def date_time_created_at(cls, value: AwareDatetime) -> datetime:
        # Strip timezone information
        return value.replace(tzinfo=None)


class Login(UserCreation):
    # Overwriting the password field from UserCreation.
    # No need for a description since the user doesn't need to
    # know about password constraints during login.
    password: str


class TokenData(BaseModel):
    # id: Optional[int] = None
    id: int


class Books(BaseModel):
    id: int
    title: str
    author: str
    release_date: date


class Book(BaseModel):
    id: int
    title: str
    author: str
    release_date: date
    total_chapters: int
    pages: int
    cover: str
    wiki: str
    summary: str
