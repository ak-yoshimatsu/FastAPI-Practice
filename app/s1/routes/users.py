from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from app.databases.session import get_section
from app.s1.models.users import UserCreate
from app.databases.models import User

router = APIRouter()


@router.get("/")
def index(session: Session = Depends(get_section)):
    result = session.execute(select(User))
    users = result.scalars().all()
    return {"data": users}


@router.post("/")
def store(users: UserCreate, session: Session = Depends(get_section)):
    users = User(name=users.name, email=users.email, password=users.password)
    session.add(users)
    session.commit()
    session.refresh(users)
    return users
