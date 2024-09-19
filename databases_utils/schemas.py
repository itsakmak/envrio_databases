__version__='1.2.2'
__author__=['Ioannis Tsakmakis']
__date_created__='2023-10-20'
__last_updated__='2024-03-01'

from pydantic import BaseModel
from typing import Optional
from enum import Enum

class AccountType(str, Enum):
    commercial = 'commercial'
    academic = 'academic'
    beta = 'beta'
    alpha = 'alpha'

# Base Models
class UsersTableBase(BaseModel):
    name: str
    email: str
    account_type: AccountType
    subscription_expires_in: float

class StationsBase(BaseModel):
    brand: str
    model: str
    code: str
    date_created: float
    last_communication: float
    status: str
    longitude: float
    latitude: float
    elevation: int
    access: dict
    name: dict
    icon_type: str

class GatewaysBase(BaseModel):
    brand: str
    model: str
    code: str
    name: str
    station_id: int

class ReapeaterUnitsBase(BaseModel):
    brand: str
    model: str
    code: str
    date_created: float
    last_communication: float
    status: str
    longitude: float
    latitude: float
    elevation: int
    name: dict
    station_id: int

class RemoteTerminalUnitsBase(BaseModel):
    brand: str
    model: str
    code: str
    date_created: float
    last_communication: float
    status: str
    longitude: float
    latitude: float
    elevation: int
    name: dict
    station_id: int
    repeater_id: int

class MonitoredParametersBase(BaseModel):
    device_type: str
    measurement: str
    unit: str
    date_created: float
    last_communication: float
    status: str
    device_height: float
    name: Optional[str] = None
    code: Optional[str] = None
    station_id: int
    repeater_id: Optional[int] = None
    rtu_id: Optional[int] = None

class FarmsRegistryBase(BaseModel):
    user_id: int
    longitude: float
    latitude: float

class FieldsRegistyBase(BaseModel):
    farm_id: int
    boundaries: dict
    soil_properties: dict

class ApplicationsBase(BaseModel):
    field_id: int
    type: str
    suggested_amount: dict
    applied_amount: dict
    applied_in: float

class AdvicesBase(BaseModel):
    field_id: int
    type: str
    status: str
    date_registered: float
    date_created: float

class MeasurementTranslationsBase(BaseModel):
    measurement: str
    el: Optional[str] = None
    en: Optional[str] = None

# Create Models

class UsersTableCreate(UsersTableBase):
    pass

class StationsCreate(StationsBase):
    pass

class GatewaysCreate(GatewaysBase):
    pass

class ReapeaterUnitsCreate(ReapeaterUnitsBase):
    pass

class RemoteTerminalUnitsCreate(RemoteTerminalUnitsBase):
    pass

class MonitoredParametersCreate(MonitoredParametersBase):
    pass

class FarmsRegistryCreate(FarmsRegistryBase):
    pass

class FieldsRegistyCreate(FieldsRegistyBase):
    pass

class ApplicationsCreate(ApplicationsBase):
    pass

class AdvicesCreate(AdvicesBase):
    pass

class MeasurementTranslationsCreate(MeasurementTranslationsBase):
    pass
