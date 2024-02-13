from fastapi import Depends

from app.s1.repositories.users import UserRepository, UserRepositoryInterface
from app.s1.schemas import users


class UserService:
    def __init__(
        self,
        repository: UserRepositoryInterface = Depends(UserRepository),
    ) -> None:
        self.repository = repository

    def getAll(self, request: users.UserRequestParams):
        return self.repository.getAll(
            name=request.name,
            email=request.email,  # type: ignore
        )

    def show(self, id: str):
        return self.repository.show(id)
