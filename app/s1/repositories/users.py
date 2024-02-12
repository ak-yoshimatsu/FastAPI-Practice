import abc
from typing import Sequence

from fastapi import Depends
from sqlmodel import select

from app.databases.models import User
from app.databases.session import Session, get_section


class UserRepositoryInterface(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def getAll(self, name: str, email: str) -> dict[str, str | int]:
        raise NotImplementedError()

    @abc.abstractmethod
    def store(self) -> dict[str, str]:
        raise NotImplementedError()

    @abc.abstractmethod
    def show(self, id: str) -> dict[str, User]:
        raise NotImplementedError()

    @abc.abstractmethod
    def update(self) -> dict[str, str]:
        raise NotImplementedError()

    @abc.abstractmethod
    def destroy(self) -> dict[str, str]:
        raise NotImplementedError()


class UserRepository(UserRepositoryInterface):
    def __init__(self, session: Session = Depends(get_section)) -> None:
        self.session = session

    def getAll(self, name: str, email: str):
        return {
            "name": name,
            "email": email,
            "id": 12231,
        }

    def store(self):
        return {"result": "store"}

    def show(self, id: str):
        # users = self.session.exec(select(User)).all()
        return {
            "result": User(
                name=id,
                password="lakfaldjfaldkal",
                email="ladfkaldj",
            )
        }

    def update(self):
        return {"result": "update"}

    def destroy(self):
        return {"result": "destroy"}
