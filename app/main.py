from fastapi import FastAPI

from app.s1.routes import users
from app.s2.routes import auth, mail, minio, patients, returns

app = FastAPI()


@app.get("/")
def index() -> dict[str, str]:
    return {"result": "index"}


app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(patients.router, prefix="/patients", tags=["patients"])
app.include_router(minio.router, prefix="/minio", tags=["minio"])
app.include_router(mail.router, prefix="/mail", tags=["mail"])
app.include_router(returns.router, prefix="/returns", tags=["returns"])
app.include_router(auth.router, prefix="/auth", tags=["auth"])
