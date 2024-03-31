from sqlalchemy.orm import Session
from passlib.context import CryptContext
from models import sql_models, api_models

crypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return crypt_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return crypt_context.hash(password)


def get_user_by_username(db: Session, username: str):
    return db.query(sql_models.User).filter(sql_models.User.username == username).first()


def authenticate_user(db: Session, username: str, password: str):
    user = get_user_by_username(db, username)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


def get_user(db: Session, user_id: int):
    return db.query(sql_models.User).filter(sql_models.User.user_id == user_id).first()


def create_user(db: Session, user: api_models.User):
    hashed_password = get_password_hash(user.password)
    db_user = sql_models.User(username=user.username, password=hashed_password, role=user.role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: int):
    db_user = get_user(db, user_id)
    if db_user:
        db.delete(db_user)
        db.commit()
        return db_user
    return None


def get_cinemas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(sql_models.Cinema).offset(skip).limit(limit).all()


def get_cinema(db: Session, cinema_id: int):
    return db.query(sql_models.Cinema).filter(sql_models.Cinema.cinema_id == cinema_id).first()


def create_cinema(db: Session, cinema: api_models.Cinema):
    # db_actor = db.query(sql_models.Actor).filter(sql_models.Actor.actor_id.in_(cinema.actors)).all()
    db_actor = db.query(sql_models.Actor).filter(sql_models.Actor.actor_id.in_([actor.actor_id for actor in cinema.actors])).all()
    db_genre = db.query(sql_models.Genre).filter(sql_models.Genre.genre_id.in_([genre.genre_id for genre in cinema.genres])).all()
    db_actor = [] if db_actor is None else db_actor
    db_genre = [] if db_genre is None else db_genre
    db_cinema = sql_models.Cinema(name=cinema.name,
                                  rating=cinema.rating,
                                  description=cinema.description,
                                  actors=db_actor,
                                  genres=db_genre,
                                  img_path=cinema.img_path)
    db.add(db_cinema)
    db.commit()
    db.refresh(db_cinema)
    return db_cinema


def delete_cinema(db: Session, cinema_id: int):
    db_cinema = db.query(sql_models.Actor).filter(sql_models.Cinema.cinema_id == cinema_id).first()
    if db_cinema:
        db.delete(db_cinema)
        db.commit()
        return db_cinema


def get_actors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(sql_models.Actor).offset(skip).limit(limit).all()


def get_actor(db: Session, actor_id: int):
    return db.query(sql_models.Actor).filter(sql_models.Actor.actor_id == actor_id).first()


def create_actor(db: Session, actor: api_models.Actor):
    db_actor = sql_models.Actor(name=actor.name,
                                birthday=actor.birthday,
                                gender=actor.gender,
                                description=actor.description,
                                img_path=actor.img_path)
    db.add(db_actor)
    db.commit()
    db.refresh(db_actor)
    return db_actor


def delete_actor(db: Session, actor_id: int):
    db_actor = db.query(sql_models.Actor).filter(sql_models.Actor.actor_id == actor_id).first()
    if db_actor:
        db.delete(db_actor)
        db.commit()
        return db_actor


def create_comment(db: Session, comment: api_models.Comment, user_id: int, cinema_id: int):
    db_comment = sql_models.Comment(source=comment.source, user_id=comment.user_id, cinema_id=comment.cinema_id)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment


def get_comment(db: Session, comment_id: int):
    return db.query(sql_models.Comment).filter(sql_models.Comment.comment_id == comment_id).first()


def delete_comment(db: Session, comment_id: int):
    db_comment = db.query(sql_models.Comment).filter(sql_models.Comment.comment_id == comment_id).first()
    if db_comment:
        db.delete(db_comment)
        db.commit()
        return db_comment


def get_comments(db: Session, cinema_id: int):
    return db.query(sql_models.Comment).filter(sql_models.Comment.cinema_id == cinema_id).all()


def get_genres(db: Session, skip: int = 0, limit: int = 100):
    return db.query(sql_models.Genre).offset(skip).limit(limit).all()


def get_genre(db: Session, genre_id: int):
    return db.query(sql_models.Genre).filter(sql_models.Genre.genre_id == genre_id).first()


def create_genre(db: Session, genre: api_models.Genre):
    db_genre = sql_models.Genre(name=genre.name)
    db.add(db_genre)
    db.commit()
    db.refresh(db_genre)
    return db_genre


def delete_genre(db: Session, genre_id: int):
    db_genre = db.query(sql_models.Actor).filter(sql_models.Genre.genre_id == genre_id).first()
    if db_genre:
        db.delete(db_genre)
        db.commit()
        return db_genre


def add_actor_cinema_relationship(db: Session, cinema_id: int, actor_id: int):
    db_cinema = db.query(sql_models.Cinema).filter(sql_models.Cinema.cinema_id == cinema_id).first()
    db_actor = db.query(sql_models.Actor).filter(sql_models.Actor.actor_id == actor_id).first()
    if db_cinema and db_actor:
        db_cinema.actors.append(db_actor)
        db.add(db_cinema)
        db.commit()
        return db_cinema


def add_genre_cinema_relationship(db: Session, cinema_id: int, genre_id: int):
    db_cinema = db.query(sql_models.Cinema).filter(sql_models.Cinema.cinema_id == cinema_id).first()
    db_genre = db.query(sql_models.Genre).filter(sql_models.Genre.genre_id == genre_id).first()
    if db_cinema and db_genre:
        db_cinema.genres.append(db_genre)
        db.add(db_cinema)
        db.commit()
        return db_cinema

def user_is_admin(user: sql_models.User):
    return user.role == 'admin'
