from pydantic import BaseModel


class UserBase(BaseModel):
    """Base User scheme"""

    email: str


class UserCreate(UserBase):
    """Input"""

    password: str


class User(UserBase):
    """Output"""

    id: int
    is_active: bool

    class Config:
        orm_mode = True
