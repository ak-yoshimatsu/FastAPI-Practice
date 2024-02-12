from fastapi import APIRouter, Depends

from app.s1.schemas import users
from app.s1.services.userServices import UserService

router = APIRouter()


@router.get("/", response_model=users.UserResponse)
def index(
    request: users.UserRequestParams = Depends(users.UserRequestParams),
    service: UserService = Depends(UserService),
):
    return service.getAll(request=request)


@router.get("/{uuid}")
def show(
    uuid: str,
    service: UserService = Depends(UserService),
):
    return service.show(id=uuid)


# @router.get("/")
# def index(session: Session = Depends(get_section)):
#     users = session.exec(select(User)).all()
#     return {"data": users}


# @router.post("/")
# def store(users: UserCreate, session: Session = Depends(get_section)):
#     users = User(name=users.name, email=users.email, password=users.password)
#     session.add(users)
#     session.commit()
#     session.refresh(users)
#     return users
