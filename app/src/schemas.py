from datetime import date, datetime

from pydantic import BaseModel, Field, EmailStr


class ContactModel(BaseModel):
    first_name: str = Field(default="", examples=["Taras", "Ostap"], min_length=1, max_length=25, title="Ім'я")
    last_name: str = Field(default="", examples=["Shevcheko", "Bulba"], min_length=1, max_length=25, title="Прізвище")
    email: EmailStr
    phone: str | None = Field(
        None, examples=["+380 44 123-4567", "+380 (44) 1234567", "+380441234567"], max_length=25, title="Номер телефону"
    )
    birthday: date | None = None
    comments: str | None = Field(default=None, title="Додаткові дані")
    favorite: bool = False


class ContactFavoriteModel(BaseModel):
    favorite: bool = False


class ContactResponse(BaseModel):
    id: int
    first_name: str | None
    last_name: str | None
    email: EmailStr | None
    phone: str | None
    birthday: date | None
    comments: str | None
    favorite: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True