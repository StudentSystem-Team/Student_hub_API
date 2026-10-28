from getpass import getpass

from app.database import Base, engine, SessionLocal
from app.models import User
from app.auth_utils import hash_password


Base.metadata.create_all(bind=engine)

name = input("Admin name: ").strip()
email = input("Admin email: ").strip().lower()
password = getpass("Admin password (minimum 8 characters): ")

if not name or not email:
    raise SystemExit("Name and email are required.")

if len(password) < 8:
    raise SystemExit("Password must contain at least 8 characters.")

db = SessionLocal()

try:
    existing = db.query(User).filter(
        User.email == email
    ).first()

    if existing:
        raise SystemExit("This email is already registered.")

    admin_user = User(
        name=name,
        email=email,
        password_hash=hash_password(password),
        role="admin",
    )

    db.add(admin_user)
    db.commit()

    print("Admin account created successfully.")

finally:
    db.close()