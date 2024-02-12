from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from sqlmodel import select

from app.databases.models import User as UserModel
from app.databases.session import Session, get_section
from app.s2.models.user import User

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.get("/user", operation_id="db get")
def read_user(session: Session = Depends(get_section)):
    users = session.exec(select(UserModel)).all()
    return {"data": users}


@router.get("/")
def read_items(token: str = Depends(oauth2_scheme)):
    return {"token": token}


@router.post("/")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    session: Session = Depends(get_section),
):
    db_items = session.exec(select(UserModel)).all()
    for item in db_items:
        print(item)

    return db_items


@router.get("/find")
def find_item(token: str):
    fake_users_db = {
        "johndoe": {
            "username": "johndoe",
            "full_name": "John Doe",
            "email": "johndoe@example.com",
            "hashed_password": "fakehashedsecret",
            "disabled": False,
        },
        "alice": {
            "username": "alice",
            "full_name": "Alice Wonderson",
            "email": "alice@example.com",
            "hashed_password": "fakehashedsecret2",
            "disabled": True,
        },
    }
    get_result = fake_users_db["alice"].get(token)
    return {"result": get_result}


class UserIn(BaseModel):
    username: str
    email: str
    password: str | None = None


@router.get("/pydantic")
def confimr_dict():
    user = UserIn(username="taro", email="sample@example.com")
    print(user)
    print(user.model_dump())
    print(user.model_dump_json())
    return user
