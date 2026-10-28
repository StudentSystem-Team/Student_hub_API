import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Load database settings from the .env file
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError(
        "DATABASE_URL is missing. Please add it to your .env file."
    )

# Some providers give URLs starting with postgres://
# SQLAlchemy needs postgresql://
if DATABASE_URL.startswith("postgres://"):
    SQLALCHEMY_DATABASE_URL = DATABASE_URL.replace(
        "postgres://", "postgresql://", 1
    )
else:
    SQLALCHEMY_DATABASE_URL = DATABASE_URL

if SQLALCHEMY_DATABASE_URL.startswith("sqlite"):
    # Local file database: very fast, good for development
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL,
        connect_args={"check_same_thread": False},
    )
else:
    # Online database (Neon PostgreSQL)
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL,
        pool_pre_ping=True,   # checks the connection is alive (Neon closes idle ones)
        pool_size=5,          # keep a few connections ready
        max_overflow=10,
        pool_recycle=300,     # refresh connections every 5 minutes
    )

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()