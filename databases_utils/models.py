from __future__ import annotations

__version__='1.4.1'
__author__=['Ioannis Tsakmakis']
__date_created__='2023-10-20'
__last_updated__='2024-09-28'

from .enum_variables import AccountType, Status, DeviceType, ApplicationType, AdviceStatus
from .engine import Base
from sqlalchemy import ForeignKey, Numeric, String, JSON, Enum as SQLAlchemyEnum
from sqlalchemy.orm import  Mapped, mapped_column
from typing import Optional

# Users
class Users(Base):
    __tablename__ = 'users_table'

    id: Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    name: Mapped[str] = mapped_column(String(500), nullable=False)
    email: Mapped[str] = mapped_column(String(500), nullable=False)
    account_type: Mapped[AccountType] = mapped_column(SQLAlchemyEnum(AccountType), nullable=False)
    subscription_expires_in: Mapped[float] = mapped_column(nullable=False)

# Devices
class Stations(Base):
    __tablename__ = 'stations'

    id: Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    brand: Mapped[str] = mapped_column(String(50))
    model: Mapped[str] = mapped_column(String(200))
    code: Mapped[str] = mapped_column(String(100),unique=True, nullable=False)
    date_created: Mapped[float] = mapped_column(nullable=False)
    last_communication: Mapped[float] = mapped_column(nullable=False)
    status: Mapped[Status] = mapped_column(SQLAlchemyEnum(Status), nullable=False)
    longitude: Mapped[float] = mapped_column(Numeric(10,8), nullable=False)
    latitude: Mapped[float] = mapped_column(Numeric(10,8), nullable=False)
    elevation: Mapped[int] = mapped_column(nullable=False)
    access: Mapped[dict|list] = mapped_column(type_=JSON, nullable=False)
    name: Mapped[dict|list] = mapped_column(type_=JSON)
    icon_type: Mapped[str] = mapped_column(String(10), nullable=False)

class GateWays(Base):
    __tablename__ = 'gateways'

    id: Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    brand: Mapped[Optional[str]] = mapped_column(String(50))
    model: Mapped[Optional[str]] = mapped_column(String(200))
    code: Mapped[Optional[str]] = mapped_column(String(100),unique=True)
    name: Mapped[Optional[str]] = mapped_column(String(500))
    station_id: Mapped[int] = mapped_column(ForeignKey('stations.id',ondelete='CASCADE'))

class RepeaterUnits(Base):
    __tablename__= 'repeater_units'

    id: Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    brand: Mapped[str] = mapped_column(String(50))
    model: Mapped[str] = mapped_column(String(200))
    code: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    date_created: Mapped[float] = mapped_column(nullable=False)
    last_communication: Mapped[float] = mapped_column(nullable=False)
    status: Mapped[Status] = mapped_column(SQLAlchemyEnum(Status), nullable=False)
    longitude: Mapped[float] = mapped_column(Numeric(10,8), nullable=False)
    latitude: Mapped[float] = mapped_column(Numeric(10,8), nullable=False)
    elevation: Mapped[int] = mapped_column(nullable=False)
    name: Mapped[dict|list] = mapped_column(type_=JSON)
    station_id: Mapped[int] = mapped_column(ForeignKey('stations.id',ondelete='CASCADE'), nullable=False)

class RemoteTerminalUnits(Base):
    __tablename__ = 'remote_terminal_units'

    id: Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    brand: Mapped[str] = mapped_column(String(50))
    model: Mapped[str] = mapped_column(String(200))
    code: Mapped[str] = mapped_column(String(100),unique=True, nullable=False)
    date_created: Mapped[float] = mapped_column(nullable=False)
    last_communication: Mapped[float] = mapped_column(nullable=False)
    status: Mapped[Status] = mapped_column(SQLAlchemyEnum(Status), nullable=False)
    longitude: Mapped[float] = mapped_column(Numeric(10,8), nullable=False)
    latitude: Mapped[float] = mapped_column(Numeric(10,8), nullable=False)
    elevation: Mapped[int] = mapped_column(nullable=False)
    name: Mapped[dict|list] = mapped_column(type_=JSON)
    station_id: Mapped[int] = mapped_column(ForeignKey('stations.id',ondelete='CASCADE'), nullable=False)
    repeater_id: Mapped[Optional[int]] = mapped_column(ForeignKey('repeater_units.id',ondelete='CASCADE'))
    
class MonitoredParameters(Base):
    __tablename__ = 'monitored_parameters'

    id: Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    device_type: Mapped[DeviceType] = mapped_column(SQLAlchemyEnum(DeviceType), nullable=False)
    measurement: Mapped[str] = mapped_column(String(100), nullable=False)
    unit: Mapped[str] = mapped_column(String(20), nullable=False)
    date_created: Mapped[float] = mapped_column(nullable=False)
    last_communication: Mapped[float] = mapped_column(nullable=False)
    status: Mapped[Status] = mapped_column(SQLAlchemyEnum(Status), nullable=False)
    device_height: Mapped[float] = mapped_column(nullable=False)
    name: Mapped[Optional[str]] = mapped_column(String(100))
    code: Mapped[Optional[str]] = mapped_column(String(100))
    station_id: Mapped[int] = mapped_column(ForeignKey('stations.id',ondelete='CASCADE'), nullable=False)
    repeater_id: Mapped[Optional[int]] = mapped_column(ForeignKey('repeater_units.id',ondelete='CASCADE'))
    rtu_id: Mapped[Optional[int]] = mapped_column(ForeignKey('remote_terminal_units.id',ondelete='CASCADE'))

# Devices Credentials
class DavisCredentials(Base):
    __tablename__ = 'davis_credentials'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] =mapped_column(ForeignKey('users_table.id', ondelete='CASCADE'), nullable=False)
    key: Mapped[str] = mapped_column(String(255), nullable=False)
    secret: Mapped[str] = mapped_column(String(255), nullable=False)

# Farms
class FarmsRegistry(Base):
    __tablename__ = 'farms_registry'

    id: Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    user_id: Mapped[int] =mapped_column(ForeignKey('users_table.id',ondelete='CASCADE'), nullable=False)
    longitude: Mapped[float] = mapped_column(type_=Numeric(10,8), nullable=False)
    latitude: Mapped[float] = mapped_column(type_=Numeric(10,8), nullable=False)

class FieldsRegisty(Base):
    __tablename__ = 'fields_registry'
    
    id: Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    farm_id: Mapped[int] = mapped_column(ForeignKey('farms_registry.id',ondelete='CASCADE'), nullable=False)
    boundaries: Mapped[dict|list] = mapped_column(type_=JSON, nullable=False)
    soil_properties: Mapped[dict|list] = mapped_column(type_=JSON) # {"hydraulic":[{"depth":20,"sat":45,"fc":35,"pwp":15,"ksat":40}], "physical":[{"depth":20,"sat":45,"fc":35,"pwp":15,"ksat":40}]}}

# Applications

class Applications(Base):
    __tablename__ = "applications_registry"

    id: Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    field_id: Mapped[int] =  mapped_column(ForeignKey('fields_registry.id',ondelete='CASCADE'), nullable=False)
    type: Mapped[ApplicationType] = mapped_column(SQLAlchemyEnum(ApplicationType), nullable=False)
    suggested_amount: Mapped[float] = mapped_column(nullable=False)
    applied_amount: Mapped[float] = mapped_column(nullable=False)
    applied_in: Mapped[float] = mapped_column(nullable=False)

# Advices

class Advices(Base):
    __tablename__ = "advices_registry"

    id: Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    field_id: Mapped[int] =  mapped_column(ForeignKey('fields_registry.id',ondelete='CASCADE'), nullable=False)
    type: Mapped[ApplicationType] = mapped_column(SQLAlchemyEnum(ApplicationType), nullable=False)
    status: Mapped[AdviceStatus] = mapped_column(SQLAlchemyEnum(AdviceStatus), nullable=False)
    date_registered: Mapped[float] = mapped_column(nullable=False)
    date_created: Mapped[float] = mapped_column(nullable=False)
