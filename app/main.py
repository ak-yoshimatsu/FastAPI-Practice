from fastapi import FastAPI

from app.s1.routes import users
from app.s2.routes import minio, patients

app = FastAPI()


@app.get("/")
def index() -> dict[str, str]:
    return {"result": "index"}


app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(patients.router, prefix="/patients", tags=["patients"])
app.include_router(minio.router, prefix="/minio", tags=["minio"])
