from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from src import config

engine = create_engine(config.POSTGRES_DB_URL)
Session = sessionmaker(bind=engine)

Base = declarative_base()
