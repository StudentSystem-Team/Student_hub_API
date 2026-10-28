from typing import Optional
from pydantic import BaseModel, ConfigDict


class ORM(BaseModel):
    model_config = ConfigDict(from_attributes=True)


# ---- AUTH ----
class UserCreate(BaseModel):
    username: str
    password: str
    role: str = "student"
    name: Optional[str] = ""

class UserLogin(BaseModel):
    username: str
    password: str


# ---- STUDENT ----
class StudentIn(BaseModel):
    name: str
    email: str
    class_name: Optional[str] = ""


class StudentOut(StudentIn, ORM):
    id: int


class StudentCreate(StudentIn): pass
class StudentUpdate(StudentIn): pass


# ---- TEACHER ----
class TeacherIn(BaseModel):
    name: str
    email: str
    subject: Optional[str] = ""


class TeacherOut(TeacherIn, ORM):
    id: int


class TeacherCreate(TeacherIn): pass


# ---- CLASS ----
class ClassIn(BaseModel):
    name: str
    section: Optional[str] = ""
    strength: int = 0


class ClassOut(ClassIn, ORM):
    id: int


class ClassCreate(ClassIn): pass


# ---- SUBJECT ----
class SubjectIn(BaseModel):
    name: str
    code: Optional[str] = ""
    teacher: Optional[str] = ""


class SubjectOut(SubjectIn, ORM):
    id: int


class SubjectCreate(SubjectIn): pass


# ---- ATTENDANCE ----
class AttendanceIn(BaseModel):
    student: str
    date: str
    status: str


class AttendanceOut(AttendanceIn, ORM):
    id: int


class AttendanceCreate(AttendanceIn): pass


# ---- EXAMINATION ----
class ExamIn(BaseModel):
    exam_name: str
    class_name: Optional[str] = ""
    date: Optional[str] = ""


class ExamOut(ExamIn, ORM):
    id: int


ExaminationIn = ExamIn
ExaminationOut = ExamOut
ExamCreate = ExamIn
ExaminationCreate = ExamIn


# ---- MARKS ----
class MarkIn(BaseModel):
    student: str
    subject: str
    marks: int = 0


class MarkOut(MarkIn, ORM):
    id: int


class MarkCreate(MarkIn): pass


# ---- RESULTS ----
class ResultIn(BaseModel):
    student: str
    grade: Optional[str] = ""
    result: Optional[str] = ""


class ResultOut(ResultIn, ORM):
    id: int


class ResultCreate(ResultIn): pass


# ---- FEES ----
class FeeIn(BaseModel):
    student: str
    amount: int = 0
    status: Optional[str] = "Pending"


class FeeOut(FeeIn, ORM):
    id: int


class FeeCreate(FeeIn): pass
class FeesIn(FeeIn): pass
class FeesOut(FeeOut): pass


# ---- ASSIGNMENTS ----
class AssignmentIn(BaseModel):
    title: str
    subject: Optional[str] = ""
    due_date: Optional[str] = ""
    description: Optional[str] = ""


class AssignmentOut(AssignmentIn, ORM):
    id: int


# ---- PAYMENTS ----
class PaymentIn(BaseModel):
    student: str
    amount: int = 0
    date: Optional[str] = ""
    method: Optional[str] = ""


class PaymentOut(PaymentIn, ORM):
    id: int


# ---- GENERIC FALLBACKS ----
class ReportIn(BaseModel):
    title: str = "Report"


class ReportOut(ReportIn, ORM):
    id: int = 1


class AdminIn(BaseModel):
    action: str = "test"


class AdminOut(AdminIn, ORM):
    id: int = 1


class PortalIn(BaseModel):
    info: str = "test"


class PortalOut(PortalIn, ORM):
    id: int = 1