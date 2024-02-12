from pydantic import BaseModel


class UserRequestParams:
    def __init__(self, name: str, email: str | None, limit: int = 100) -> None:
        self.name = name
        self.email = email
        self.limit = limit


class UserResponse(BaseModel):
    id: int
    name: str
    email: str
