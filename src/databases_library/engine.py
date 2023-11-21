__version__='1.0.1'
__author__='Ioannis Tsakmakis'
__date_created__='2023-11-21'

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
import json

with open('mysql_config.json','r') as f:
    config = json.load(f)

engine = create_engine(url=f'{config["DBAPI"]}://{config["username"]}:{config['password']}@{config["host-ip"]}/{config["database"]}', echo=True)

LocalSession = sessionmaker(bind=engine,expire_on_commit=True)

class Base(DeclarativeBase):
    pass

