from app.database import Base, engine
from app import models  # Load all model definitions

print("Creating missing database tables...")

Base.metadata.create_all(bind=engine)

print("Database tables are ready!")