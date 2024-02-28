from sqlmodel import Column, Field, Relationship, SQLModel, String


class User(SQLModel, table=True):
    __tablename__ = "users"

    id: int | None = Field(default=None, primary_key=True, index=True)
    name: str = Field(max_length=32)
    email: str = Field(
        max_length=64,
        title="メールアドレス",
        description="メールアドレスを格納する",
    )
    password: str = Field(max_length=64)


class Patient(SQLModel, table=True):
    __tablename__ = "patients"

    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(max_length=32, sa_column=Column(String(32)))
    age: int | None = Field(nullable=True)


# class Posts(SQLModel, table=True):
#     id: int | None = Field(default=None, primary_key=True)
#     user_id: int | None = Field(default=None, foreign_key="users.id")
#     title: str = Field(sa_column=Column(String(32)))
#     content: str

#     user: User | None = Relationship(back_populates="has_posts")


# class Comments(SQLModel, table=True):
#     id: int | None = Field(default=None, primary_key=True)
#     post_id: int | None = Field(default=None, foreign_key="posts.id")
#     content: str
