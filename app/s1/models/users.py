from typing import Optional

from sqlmodel import Field, SQLModel

from app.databases import Base

SQLModel.metadata = Base.metadata


class TestUser(SQLModel, table=True):
    __table_args__ = {"extend_existing": True}
    __tablename__ = "test_users"
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=32)
    email: str = Field(max_length=64)
    password: str = Field(max_length=64)
