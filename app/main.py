# from logging import StreamHandler, basicConfig, getLogger
import logging

from fastapi import FastAPI

from app.s1.routes import users
from app.s2.routes import mail, minio, patients

logger = logging.getLogger("uvicorn")

file_handler = logging.FileHandler("app.log")

formatter = logging.Formatter("[%(levelname)s] %(asctime)s - %(message)s")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.setLevel(logging.INFO)

logging.basicConfig(level=logging.INFO)

app = FastAPI()


@app.get("/")
def index() -> dict[str, str]:
    logging.info("retuning index INFO")
    return {"result": "index"}


app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(patients.router, prefix="/patients", tags=["patients"])
app.include_router(minio.router, prefix="/minio", tags=["minio"])
app.include_router(mail.router, prefix="/mail", tags=["mail"])
