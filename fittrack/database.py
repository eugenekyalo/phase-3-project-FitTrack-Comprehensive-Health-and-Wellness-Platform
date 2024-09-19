from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fittrack.models import Base

DATABASE_URL = 'sqlite:///fittrack.db'

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)
