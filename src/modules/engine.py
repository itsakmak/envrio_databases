__version__='1.0.0'
__author__='Ioannis Tsakmakis'
__date_created__='2023-10-31'

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

engine = create_engine("mysql+mysqlconnector://username:password@host-ip/database", echo=True)

LocalSession = sessionmaker(bind=engine,expire_on_commit=True)

class Base(DeclarativeBase):
    pass

