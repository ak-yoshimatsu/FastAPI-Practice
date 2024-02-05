from fastapi import APIRouter, Depends
from app.databases import get_section
from app.s1.models.users import UserCreate, TestUser
from sqlmodel import Session, select

router = APIRouter()


@router.get("/")
def index(session: Session = Depends(get_section)):
    result = session.execute(select(TestUser))
    users = result.scalars().all()
    return {"data": users}


@router.post("/")
def store(users: UserCreate, session: Session = Depends(get_section)):
    users = TestUser(
        name=users.name, email=users.email, password=users.password
    )
    session.add(users)
    session.commit()
    session.refresh(users)
    return users
