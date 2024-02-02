__version__='1.1.0'
__author__=['Ioannis Tsakmakis']
__date_created__='2023-10-20'
__last_updated__='2024-02-02'

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
import json

with open('credentials.json','r') as f:
    credentials = json.load(f)

with open(credentials['mysql'],'r') as f:
    config = json.load(f)

# sqlalchemy logging path
logging_path = credentials['sqlalchemy_logging_path']

# Creating sqlalchemy engine
engine = create_engine(url=f'{config["DBAPI"]}://{config["username"]}:{config['password']}@{config["host-ip"]}/{config["database"]}',
                         pool_size=30, max_overflow=5, pool_recycle=7200)


SessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass
