from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import crud
from models import api_models, sql_models
from database import SessionLocal, engine
from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from datetime import datetime, timedelta, timezone
from typing import List
import time

SECRET_KEY = "YOUR_SECRET_KEY"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 100

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

sql_models.Base.metadata.create_all(bind=engine)
router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_access_token(data: dict, expires_delta=None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = api_models.TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = crud.get_user_by_username(db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user


@router.post("/token", response_model=api_models.Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = crud.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )

    expiration = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    expiration_timestamp = int(expiration.replace(tzinfo=timezone.utc).timestamp())

    return {"access_token": access_token,
            "token_type": "bearer",
            "role": user.role,
            "exp": expiration_timestamp}


@router.post("/users/", response_model=api_models.User)
def create_user(user: api_models.User, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return crud.create_user(db=db, user=user)


@router.delete("/users/{user_id}", response_model=api_models.User)
def delete_user(user_id: int, db: Session = Depends(get_db), current_user: sql_models.User = Depends(get_current_user)):
    if not crud.user_is_admin(current_user):
        raise HTTPException(status_code=403, detail="Not authorized to delete user")
    if current_user.id == user_id:
        raise HTTPException(status_code=403, detail="Cannot delete yourself")
    user = crud.get_user(db, user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.delete_user(db, user_id)


@router.post("/cinema/", response_model=api_models.Cinema)
def create_cinema(cinema: api_models.Cinema, db: Session = Depends(get_db),
                  current_user: sql_models.User = Depends(get_current_user)):
    if not crud.user_is_admin(current_user):
        raise HTTPException(status_code=403, detail="Not authorized to create cinema")
    return crud.create_cinema(db=db, cinema=cinema)


@router.get("/cinema/", response_model=List[api_models.Cinema])
def get_cinemas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    cinemas = crud.get_cinemas(db, skip=skip, limit=limit)
    return cinemas


@router.get("/cinema/{cinema_id}", response_model=api_models.Cinema)
def get_cinema(cinema_id: int, db: Session = Depends(get_db)):
    db_cinema = crud.get_cinema(db, cinema_id=cinema_id)
    if db_cinema is None:
        raise HTTPException(status_code=404, detail="Cinema not found")
    return db_cinema


@router.delete("/cinema/{cinema_id}", response_model=api_models.Cinema)
def delete_cinema(cinema_id: int, db: Session = Depends(get_db), current_user: sql_models.User = Depends(get_current_user)):
    if not crud.user_is_admin(current_user):
        raise HTTPException(status_code=403, detail="Not authorized to delete cinema")
    user = crud.get_cinema(db, cinema_id=cinema_id)
    if user is None:
        raise HTTPException(status_code=404, detail="Cinema not found")
    return crud.delete_cinema(db, cinema_id)


@router.post("/genre/", response_model=api_models.Genre)
def create_genre(genre: api_models.Genre, db: Session = Depends(get_db),
                 current_user: sql_models.User = Depends(get_current_user)):
    if not crud.user_is_admin(current_user):
        raise HTTPException(status_code=403, detail="Not authorized to create cinema")
    return crud.create_genre(db=db, genre=genre)


@router.get("/genre/", response_model=List[api_models.Genre])
def get_genres(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    genres = crud.get_genres(db, skip=skip, limit=limit)
    return genres


@router.get("/genre/{genre_id}", response_model=api_models.Genre)
def get_genre(genre_id: int, db: Session = Depends(get_db)):
    db_genre = (crud.get_genre(db, genre_id=genre_id))
    if db_genre is None:
        raise HTTPException(status_code=404, detail="Genre not found")
    return db_genre


@router.delete("/genre/{genre_id}", response_model=api_models.Genre)
def delete_genre(genre_id: int, db: Session = Depends(get_db),
                 current_user: sql_models.User = Depends(get_current_user)):
    if not crud.user_is_admin(current_user):
        raise HTTPException(status_code=403, detail="Not authorized to delete genre")
    user = crud.get_genre(db, genre_id=genre_id)
    if user is None:
        raise HTTPException(status_code=404, detail="Genre not found")
    return crud.delete_genre(db, genre_id)


@router.post("/actor/", response_model=api_models.Actor)
def create_actor(actor: api_models.Actor, db: Session = Depends(get_db),
                 current_user: sql_models.User = Depends(get_current_user)):
    if not crud.user_is_admin(current_user):
        raise HTTPException(status_code=403, detail="Not authorized to create actor")
    return crud.create_actor(db=db, actor=actor)


@router.get("/actor/", response_model=List[api_models.Actor])
def get_actors(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    actors = crud.get_actors(db, skip=skip, limit=limit)
    return actors


@router.get("/actor/{actor_id}", response_model=api_models.Actor)
def get_genre(actor_id: int, db: Session = Depends(get_db)):
    db_actor = (crud.get_actor(db, actor_id=actor_id))
    if db_actor is None:
        raise HTTPException(status_code=404, detail="Actor not found")
    return db_actor


@router.delete("/actor/{actor_id}", response_model=api_models.Actor)
def delete_actor(actor_id: int, db: Session = Depends(get_db),
                 current_user: sql_models.User = Depends(get_current_user)):
    if not crud.user_is_admin(current_user):
        raise HTTPException(status_code=403, detail="Not authorized to delete actor")
    user = crud.get_actor(db, actor_id=actor_id)
    if user is None:
        raise HTTPException(status_code=404, detail="Actor not found")
    return crud.delete_actor(db, actor_id)

