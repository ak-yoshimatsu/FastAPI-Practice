from sqlmodel import Session, create_engine
from app.config import env


path = (
    "mysql+pymysql://"
    + str(env.MYSQL_USER)
    + ":"
    + str(env.MYSQL_PASSWORD)
    + "@"
    + str(env.MYSQL_HOST)
    + ":"
    + str(env.MYSQL_PORT)
    + "/"
    + str(env.MYSQL_DATABASE)
)

# Engine の作成
Engine = create_engine(path, echo=True)


def get_section():
    with Session(Engine) as session:
        yield session
