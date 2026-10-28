from app.database import Base, engine, SessionLocal
from app import models

Base.metadata.create_all(bind=engine)

DATA = {
    models.SchoolClass: [
        dict(name="BCA 1st Year", section="A", strength=60),
        dict(name="BCA 2nd Year", section="A", strength=58),
        dict(name="BCA 3rd Year", section="A", strength=55),
        dict(name="B.Sc 1st Year", section="B", strength=62),
        dict(name="B.Sc 2nd Year", section="B", strength=57),
        dict(name="B.Com 1st Year", section="C", strength=70),
        dict(name="B.Com 2nd Year", section="C", strength=66),
        dict(name="MBA 1st Year", section="D", strength=40),
    ],
    models.Subject: [
        dict(name="Python Programming", code="CS101", teacher="Dr. Rao"),
        dict(name="Data Structures", code="CS102", teacher="Ms. Priya"),
        dict(name="Database Management", code="CS103", teacher="Mr. Kumar"),
        dict(name="Web Technologies", code="CS104", teacher="Ms. Anitha"),
        dict(name="Mathematics", code="MA101", teacher="Dr. Reddy"),
        dict(name="Operating Systems", code="CS105", teacher="Mr. Sharma"),
        dict(name="Computer Networks", code="CS106", teacher="Ms. Lakshmi"),
        dict(name="English Communication", code="EN101", teacher="Mrs. Devi"),
    ],
    models.Assignment: [
        dict(title="Python Basics Worksheet", subject="Python Programming", due_date="2026-11-03", description="Solve 10 problems on loops and functions"),
        dict(title="Linked List Program", subject="Data Structures", due_date="2026-11-05", description="Implement singly linked list operations"),
        dict(title="ER Diagram", subject="Database Management", due_date="2026-11-07", description="Draw an ER diagram for a library system"),
        dict(title="Portfolio Webpage", subject="Web Technologies", due_date="2026-11-10", description="Build a personal portfolio using HTML and CSS"),
        dict(title="Matrix Problems", subject="Mathematics", due_date="2026-11-12", description="Complete exercise 4.2 and 4.3"),
        dict(title="Process Scheduling Report", subject="Operating Systems", due_date="2026-11-14", description="Write a report on CPU scheduling algorithms"),
        dict(title="Network Topologies", subject="Computer Networks", due_date="2026-11-17", description="Compare bus, star and ring topologies"),
        dict(title="Presentation Skills", subject="English Communication", due_date="2026-11-20", description="Prepare a 5 minute presentation"),
    ],
    models.Examination: [
        dict(exam_name="Internal Test 1 - Python", class_name="BCA 1st Year", date="2026-11-18"),
        dict(exam_name="Internal Test 1 - Data Structures", class_name="BCA 1st Year", date="2026-11-19"),
        dict(exam_name="Internal Test 1 - DBMS", class_name="BCA 2nd Year", date="2026-11-20"),
        dict(exam_name="Internal Test 1 - Web Tech", class_name="BCA 2nd Year", date="2026-11-21"),
        dict(exam_name="Mid Semester - Mathematics", class_name="B.Sc 1st Year", date="2026-11-24"),
        dict(exam_name="Mid Semester - Operating Systems", class_name="BCA 3rd Year", date="2026-11-25"),
        dict(exam_name="Mid Semester - Networks", class_name="BCA 3rd Year", date="2026-11-26"),
        dict(exam_name="Mid Semester - English", class_name="B.Com 1st Year", date="2026-11-27"),
    ],
    models.Attendance: [
        dict(student="chinnu", date="2026-10-19", status="Present"),
        dict(student="chinnu", date="2026-10-20", status="Present"),
        dict(student="chinnu", date="2026-10-21", status="Absent"),
        dict(student="chinnu", date="2026-10-22", status="Present"),
        dict(student="chinnu", date="2026-10-23", status="Present"),
        dict(student="chinnu", date="2026-10-24", status="Late"),
        dict(student="chinnu", date="2026-10-26", status="Present"),
        dict(student="chinnu", date="2026-10-27", status="Present"),
    ],
    models.Result: [
        dict(student="chinnu", grade="A", result="Pass - Python Programming"),
        dict(student="chinnu", grade="B+", result="Pass - Data Structures"),
        dict(student="chinnu", grade="A", result="Pass - Database Management"),
        dict(student="chinnu", grade="B", result="Pass - Web Technologies"),
        dict(student="chinnu", grade="A+", result="Pass - Mathematics"),
        dict(student="chinnu", grade="B", result="Pass - Operating Systems"),
        dict(student="chinnu", grade="C", result="Pass - Computer Networks"),
        dict(student="chinnu", grade="A", result="Pass - English Communication"),
    ],
    models.Fee: [
        dict(student="chinnu", amount=25000, status="Paid"),
        dict(student="chinnu", amount=25000, status="Paid"),
        dict(student="chinnu", amount=5000, status="Paid"),
        dict(student="chinnu", amount=3000, status="Pending"),
        dict(student="chinnu", amount=2000, status="Pending"),
        dict(student="chinnu", amount=1500, status="Paid"),
        dict(student="chinnu", amount=1000, status="Pending"),
        dict(student="chinnu", amount=500, status="Paid"),
    ],
    models.Payment: [
        dict(student="chinnu", amount=25000, date="2026-06-10", method="Online"),
        dict(student="chinnu", amount=25000, date="2026-08-12", method="UPI"),
        dict(student="chinnu", amount=5000, date="2026-08-20", method="Cash"),
        dict(student="chinnu", amount=1500, date="2026-09-05", method="Card"),
        dict(student="chinnu", amount=500, date="2026-09-18", method="UPI"),
        dict(student="chinnu", amount=2000, date="2026-10-01", method="Online"),
        dict(student="chinnu", amount=3000, date="2026-10-10", method="Cash"),
        dict(student="chinnu", amount=1000, date="2026-10-20", method="UPI"),
    ],
}

db = SessionLocal()
for model, rows in DATA.items():
    if db.query(model).count() == 0:
        db.add_all([model(**r) for r in rows])
        print(f"Added {len(rows)} rows to {model.__tablename__}")
    else:
        print(f"Skipped {model.__tablename__} (already has data)")
db.commit()
db.close()