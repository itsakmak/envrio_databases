from __future__ import annotations

__version__='1.0.1'
__author__='Ioannis Tsakmakis'
__date_created__='2023-11-23'

from sqlalchemy import ForeignKey, Numeric, String, JSON
from sqlalchemy.orm import  Mapped, mapped_column
from databases_library.engine import Base, create_db_engine
from typing import Optional

# Users
class Users(Base):
    __tablename__ = 'users_table'

    id: Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    name: Mapped[str] = mapped_column(String(500))
    email: Mapped[str] = mapped_column(String(500))
    subscription_expires_in: Mapped[str] = mapped_column(String(20))

# Devices
class Stations(Base):
    __tablename__ = 'stations'

    id: Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    brand: Mapped[str] = mapped_column(String(50))
    model: Mapped[str] = mapped_column(String(200))
    code: Mapped[str] = mapped_column(String(100),unique=True)
    date_created: Mapped[str] = mapped_column(String(24))
    longitude: Mapped[float] = mapped_column(Numeric(10,8))
    latitude: Mapped[float] = mapped_column(Numeric(10,8))
    elevation: Mapped[int]
    access: Mapped[dict|list] = mapped_column(type_=JSON)
    name: Mapped[dict|list] = mapped_column(type_=JSON)
    icon_type: Mapped[str] = mapped_column(String(10))

class GateWays(Base):
    __tablename__ = 'gateways'

    id: Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    brand: Mapped[Optional[str]] = mapped_column(String(50))
    model: Mapped[Optional[str]] = mapped_column(String(200))
    code: Mapped[Optional[str]] = mapped_column(String(100),unique=True)
    name: Mapped[Optional[str]] = mapped_column(String(500))
    station_id: Mapped[int] = mapped_column(ForeignKey('stations.id',ondelete='CASCADE'))

class RemoteTerminalUnits(Base):
    __tablename__ = 'remote_terminal_units'

    id: Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    brand: Mapped[str] = mapped_column(String(50))
    model: Mapped[str] = mapped_column(String(200))
    code: Mapped[str] = mapped_column(String(100),unique=True)
    longitude: Mapped[float] = mapped_column(Numeric(10,8))
    latitude: Mapped[float] = mapped_column(Numeric(10,8))
    elevation: Mapped[int]
    name: Mapped[dict|list] = mapped_column(type_=JSON)
    station_id: Mapped[int] = mapped_column(ForeignKey('stations.id',ondelete='CASCADE'))
    
class SensorsMeters(Base):
    __tablename__ = 'sensors_meters'

    id: Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    type: Mapped[str] = mapped_column(String(7))
    measurement: Mapped[str] = mapped_column(String(100))
    unit: Mapped[str] = mapped_column(String(20))
    gauge_height: Mapped[float]
    name: Mapped[Optional[str]] = mapped_column(String(100))
    code: Mapped[Optional[str]] = mapped_column(String(100))
    station_id: Mapped[int] = mapped_column(ForeignKey('stations.id',ondelete='CASCADE'))
    rtu_id: Mapped[Optional[int]] = mapped_column(ForeignKey('remote_terminal_units.id',ondelete='CASCADE'))

# Farms

class FarmsRegistry(Base):
    __tablename__ = 'farms_registry'

    id: Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    user_id: Mapped[int] =mapped_column(ForeignKey('users_table.id',ondelete='CASCADE'))
    longitude: Mapped[float] = mapped_column(type_=Numeric(10,8))
    latitude: Mapped[float] = mapped_column(type_=Numeric(10,8))

class FieldsRegisty(Base):
    __tablename__ = 'fields_registry'
    
    id: Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    farm_id: Mapped[int] = mapped_column(ForeignKey('farms_registry.id',ondelete='CASCADE'))
    boundaries: Mapped[dict|list] = mapped_column(type_=JSON)
    soil_properties: Mapped[dict|list] = mapped_column(type_=JSON) # {"hydraulic":[{"depth":20,"sat":45,"fc":35,"pwp":15,"ksat":40}]} {"physical":[{"depth":20,"sat":45,"fc":35,"pwp":15,"ksat":40}]}

# Applications

class Applications(Base):
    __tablename__ = "applications_registry"

    id: Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    field_id: Mapped[int] =  mapped_column(ForeignKey('fields_registry.id',ondelete='CASCADE'))
    type: Mapped[str] = mapped_column(String(10))
    suggested_amount: Mapped[float]
    applied_amount: Mapped[float]
    applied_in: Mapped[str] = mapped_column(String(20))

# Advices

class Advices(Base):
    __tablename__ = "advices_registry"

    id: Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    field_id: Mapped[int] =  mapped_column(ForeignKey('fields_registry.id',ondelete='CASCADE'))
    type: Mapped[str] = mapped_column(String(10))
    status: Mapped[str] = mapped_column(String(10))
    date_registered: Mapped[str] = mapped_column(String(20))
    date_created: Mapped[str] = mapped_column(String(20))

# Measurements Languages

class MeasurementTranslations(Base):
    __tablename__ = 'measurement_translations'

    measurement: Mapped[str] = mapped_column(String(100),primary_key=True)
    el: Mapped[Optional[str]] = mapped_column(String(800))
    en: Mapped[Optional[str]] = mapped_column(String(800))

Base.metadata.create_all(create_db_engine())
