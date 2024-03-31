from sqlalchemy import Column, Integer, String, ForeignKey, Float, Date, Table
from sqlalchemy.orm import relationship
from database import Base

actor_cinema = Table('actor_cinema', Base.metadata,
                     Column('actor_id', Integer, ForeignKey('actors.actor_id')),
                     Column('cinema_id', Integer, ForeignKey('cinemas.cinema_id')))

genre_cinema = Table('genre_cinema', Base.metadata,
                     Column('genre_id', Integer, ForeignKey('genres.genre_id')),
                     Column('cinema_id', Integer, ForeignKey('cinemas.cinema_id')))


class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer,
                     primary_key=True,
                     index=True,
                     unique=True,
                     nullable=False,
                     autoincrement=True)
    username = Column(String,
                      unique=True,
                      index=True)
    password = Column(String)
    role = Column(String,
                  default="user")


class Actor(Base):
    __tablename__ = "actors"
    actor_id = Column(Integer,
                      primary_key=True,
                      index=True,
                      unique=True,
                      nullable=False,
                      autoincrement=True)
    name = Column(String,
                  unique=True,
                  index=True)
    birthday = Column(Date)
    gender = Column(String)
    description = Column(String)
    cinemas = relationship('Cinema',
                           secondary=actor_cinema,
                           back_populates='actors')
    img_path = Column(String)


class Genre(Base):
    __tablename__ = "genres"
    genre_id = Column(Integer,
                      primary_key=True,
                      index=True,
                      unique=True,
                      nullable=False,
                      autoincrement=True)
    name = Column(String)
    cinemas = relationship('Cinema',
                           secondary=genre_cinema,
                           back_populates='genres')


class Cinema(Base):
    __tablename__ = "cinemas"
    cinema_id = Column(Integer,
                       primary_key=True,
                       index=True,
                       unique=True,
                       nullable=False,
                       autoincrement=True)
    name = Column(String,
                  unique=True,
                  index=True)
    rating = Column(Float)
    actors = relationship('Actor',
                          secondary=actor_cinema,
                          back_populates='cinemas')
    genres = relationship('Genre',
                          secondary=genre_cinema,
                          back_populates='cinemas')
    description = Column(String)
    img_path = Column(String)


class Comment(Base):
    __tablename__ = "comments"
    comment_id = Column(Integer,
                        primary_key=True,
                        index=True,
                        unique=True,
                        nullable=False,
                        autoincrement=True)
    user_id = Column(Integer,
                     ForeignKey("users.user_id"))
    cinema_id = Column(Integer,
                       ForeignKey("cinemas.cinema_id"))
    source = Column(String)
