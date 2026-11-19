from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Replace with your actual PostgreSQL connection string from environment variables
SQLALCHEMY_DATABASE_URL = "postgresql://user:password@localhost:5432/drportal_db"

# Create SQLAlchemy engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Session factory for handling database transactions in API endpoints
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Centralized Base class for all models
Base = declarative_base()

# Dependency for FastAPI endpoints to get a DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# TODO: Change the database url to use environment variables for production deployment.