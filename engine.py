__version__=1.0
__author__='Ioannis Tsakmakis'
__date_created__='2023-10-31'

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from typing import Any

engine = create_engine("mysql+mysqlconnector://nkokkos:!nkEnvRIo828521@83.212.135.202/envrio_core", echo=True)

LocalSession = sessionmaker(bind=engine,expire_on_commit=True)

class Base(DeclarativeBase):
    pass

