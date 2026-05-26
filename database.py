#main_database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


#setting up the url to tell sqlAlchmey, where our database actually is

SQLALCHEMY_DATABASE_URL = "sqlite:///./final_Blog_main.db"


#setting up the actual connection to database which acts as an actual bridge between python and database file

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass


def get_db():
    with sessionlocal() as db:
        yield db
