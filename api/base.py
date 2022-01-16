from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from dotenv import load_dotenv
import os

load_dotenv()
base = declarative_base()

conn = os.getenv('DATABASE_URL')
engine = create_engine(conn, echo=False)
Session = Session(engine)
base.metadata.create_all(engine)
