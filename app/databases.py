# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base

from sqlmodel import create_engine, Session

path = "mysql+pymysql://fastapi:drowssap@db:3306/fastapi"

# Engine の作成
Engine = create_engine(path, echo=True)
# Base = declarative_base()


def get_section():
    with Session(Engine) as session:
        yield session
