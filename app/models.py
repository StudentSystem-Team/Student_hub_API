from sqlalchemy import Column, Integer, String
from app.database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    role = Column(String)


class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    class_name = Column(String)


class Teacher(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    subject = Column(String)


class SchoolClass(Base):
    __tablename__ = "classes"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    section = Column(String)
    strength = Column(Integer, default=0)


class Subject(Base):
    __tablename__ = "subjects"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    code = Column(String)
    teacher = Column(String)


class Attendance(Base):
    __tablename__ = "attendance"
    id = Column(Integer, primary_key=True, index=True)
    student = Column(String)
    date = Column(String)
    status = Column(String)


class Examination(Base):
    __tablename__ = "examinations"
    id = Column(Integer, primary_key=True, index=True)
    exam_name = Column(String)
    class_name = Column(String)
    date = Column(String)


class Mark(Base):
    __tablename__ = "marks"
    id = Column(Integer, primary_key=True, index=True)
    student = Column(String)
    subject = Column(String)
    marks = Column(Integer)


class Result(Base):
    __tablename__ = "results"
    id = Column(Integer, primary_key=True, index=True)
    student = Column(String)
    grade = Column(String)
    result = Column(String)


class Fee(Base):
    __tablename__ = "fees"
    id = Column(Integer, primary_key=True, index=True)
    student = Column(String)
    amount = Column(Integer)
    status = Column(String)


class Assignment(Base):
    __tablename__ = "assignments"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    subject = Column(String)
    due_date = Column(String)
    description = Column(String)


class Payment(Base):
    __tablename__ = "payments"
    id = Column(Integer, primary_key=True, index=True)
    student = Column(String)
    amount = Column(Integer)
    date = Column(String)
    method = Column(String)


# Aliases used by other files
Class = SchoolClass
ExamResult = Result
Results = Result
ExamResults = Result