from sqlmodel import SQLModel


class PatientCreate(SQLModel):
    name: str
    age: int
