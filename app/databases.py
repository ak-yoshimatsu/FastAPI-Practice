from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

path = "mysql+pymysql://fastapi:@127.0.0.1:3306/drowssap"

# Engine の作成
Engine = create_engine(path, encoding="utf-8", echo=False)
Base = declarative_base()
