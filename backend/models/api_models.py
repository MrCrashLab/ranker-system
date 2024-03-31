from pydantic import BaseModel
from datetime import date
from typing import List, ForwardRef

Cinema = ForwardRef("Cinema")


class User(BaseModel):
    user_id: int
    username: str
    password: str
    role: str


class Actor(BaseModel):
    actor_id: int
    name: str
    birthday: date
    gender: str
    description: str
    img_path: str


class Genre(BaseModel):
    genre_id: int
    name: str


class Cinema(BaseModel):
    cinema_id: int
    name: str
    rating: float
    actors: list[Actor]
    genres: list[Genre]
    description: str
    img_path: str


class Comment(BaseModel):
    comment_id: int
    user_id: int
    cinema_id: int
    source: str

class Token(BaseModel):
    access_token: str
    token_type: str
    role: str
    exp: int


class TokenData(BaseModel):
    username: str = None