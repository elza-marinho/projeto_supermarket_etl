import os
from dotenv import load_dotenv
from sqlalchemy import create_engine


load_dotenv()

SUPERMARKET_DATABASE_URL = os.getenv("SUPERMARKET_DATABASE_URL")

engine= create_engine(SUPERMARKET_DATABASE_URL)

