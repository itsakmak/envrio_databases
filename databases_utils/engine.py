__version__='1.1.0'
__author__=['Ioannis Tsakmakis']
__date_created__='2023-10-20'
__last_updated__='2024-02-02'

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
import json, os

with open(f'{os.path.dirname(os.path.abspath(__file__))}/local_path.json','r') as f:
    local_path = json.load(f)

with open(f'{local_path['local_path']}/credentials.json') as f:
    credentials = json.load(f)

with open(credentials['mysql_dev'],'r') as f:
    config = json.load(f)

# Creating sqlalchemy engine
engine = create_engine(url=f'{config["DBAPI"]}://{config["username"]}:{config['password']}@{config["host-ip"]}/{config["database"]}',
                       pool_size=30, max_overflow=5, pool_recycle=7200)
    

SessionLocal = sessionmaker(bind=engine)

logging_path = credentials['sqlalchemy_logging_path']


class Base(DeclarativeBase):
    pass
