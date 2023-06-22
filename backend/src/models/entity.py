from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from src import config

db_url = f'{config.POSTGRES_TARGET}:5432'
db_name = config.POSTGRES_DB
db_user = config.POSTGRES_USER
db_password = config.POSTGRES_PASSWORD

engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_url}/{db_name}')

Session = sessionmaker(bind=engine)

Base = declarative_base()
