from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import Base, engine
from app import models
from app.routes import (
    admin, attendance, auth, classes, examinations, fees, portal, reports,
    students, teachers, subjects, marks, results, assignments, payments,
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title="Student Management System API",
    version="1.0.0",
    lifespan=lifespan,
    swagger_ui_parameters={"persistAuthorization": True},
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(students.router, prefix="/api/students", tags=["Students"])
app.include_router(teachers.router, prefix="/api/teachers", tags=["Teachers"])
app.include_router(classes.router, prefix="/api/classes", tags=["Classes"])
app.include_router(subjects.router, prefix="/api/subjects", tags=["Subjects"])
app.include_router(attendance.router, prefix="/api/attendance", tags=["Attendance"])
app.include_router(examinations.router, prefix="/api/exams", tags=["Exams"])
app.include_router(marks.router, prefix="/api/marks", tags=["Marks"])
app.include_router(results.router, prefix="/api/results", tags=["Results"])
app.include_router(fees.router, prefix="/api/fees", tags=["Fees"])
app.include_router(assignments.router, prefix="/api/assignments", tags=["Assignments"])
app.include_router(payments.router, prefix="/api/payments", tags=["Payments"])
app.include_router(reports.router, prefix="/api/reports", tags=["Reports"])
app.include_router(portal.router, tags=["Portal"])
app.include_router(admin.router, prefix="/api/admin", tags=["Admin"])


@app.get("/", tags=["Root"])
def root():
    return {"message": "Backend Running"}