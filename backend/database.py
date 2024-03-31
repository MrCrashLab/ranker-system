from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import configparser

metadata = MetaData()

config = configparser.ConfigParser()
config.read("config.ini")

SQLALCHEMY_DATABASE_URL = f"postgresql://{config['postgres']['username']}:{config['postgres']['password']}@{config['postgres']['host']}:5432/{config['postgres']['dbname']}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base(metadata=metadata)
