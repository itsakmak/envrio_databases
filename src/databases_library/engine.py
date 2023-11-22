__version__='1.0.2'
__author__='Ioannis Tsakmakis'
__date_created__='2023-11-22'

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
import json

with open('mysql_config.json','r') as f:
    config = json.load(f)

engine = create_engine(url=f'{config["DBAPI"]}://{config["username"]}:{config['password']}@{config["host-ip"]}/{config["database"]}', 
                       pool_pre_ping=True)
class Base(DeclarativeBase):
    pass
