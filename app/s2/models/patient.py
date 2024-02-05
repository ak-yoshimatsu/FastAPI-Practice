from typing import Optional
from sqlmodel import Field, SQLModel


class Patient(SQLModel, table=True):
    __tablename__ = "patients"

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=32)
    age: int = Field()


class PatientCreate(SQLModel):
    name: str
    age: int
