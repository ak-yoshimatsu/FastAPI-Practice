from sqlmodel import Session, create_engine

path = "mysql+pymysql://fastapi:drowssap@db:3306/fastapi"

# Engine の作成
Engine = create_engine(path, echo=True)


def get_section():
    with Session(Engine) as session:
        yield session
