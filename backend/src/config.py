from dotenv import load_dotenv
import os
from sys import platform

load_dotenv()

POSTGRES_TARGET = "localhost"
if (container_name := os.environ.get('DB_CONTAINER_NAME')):
    POSTGRES_TARGET = container_name
POSTGRES_DB = os.environ.get('POSTGRES_DB')
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
POSTGRES_USER = os.environ.get('POSTGRES_USER')
AWS_ACCESS_KEY = os.environ.get('AWS_ACCESS_KEY')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_BUCKET_NAME = os.environ.get('AWS_BUCKET_NAME')
POSTGRES_DB_URL = os.environ.get('POSTGRES_DB_URL')
ADMIN_TOKEN = os.environ.get('ADMIN_TOKEN')
