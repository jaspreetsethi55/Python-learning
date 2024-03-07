from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

##defining database path/url
SQLALCHAMY_DATABASE_URL = 'sqlite:///./blog.db'  #'sqlite:///./memory' -- for memory database

#creating database engine
engine = create_engine(SQLALCHAMY_DATABASE_URL, connect_args = {"check_same_thread": False})
#create engine('sqlite:///./memory',echo=True) -- for creating database im memory

##creating local session
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

#declaring model
Base = declarative_base() #base model for declaring our model


