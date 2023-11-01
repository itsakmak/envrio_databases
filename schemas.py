__version__=1.0
__author__='Ioannis Tsakmakis'
__date_created__='2023-10-31'

from pydantic import BaseModel
from typing import Optional

# Base Models
class UsersTableBase(BaseModel):
    name: str
    email: str
    subscription_expires_in: str

class StationsBase(BaseModel):
    brand: str
    model: str
    code: str
    date_created: str
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

class RemoteTerminalUnitsBase(BaseModel):
    brand: str
    model: str
    code: str
    longitude: float
    latitude: float
    elevation: int
    name: dict
    station_id: int

class SensorsMetersBase(BaseModel):
    type: str
    measurement: str
    unit: str
    gauge_height: float
    name: Optional[str] = None
    code: Optional[str] = None
    station_id: int
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
    suggested_amount: float
    applied_amount: float
    applied_in: str

class AdvicesBase(BaseModel):
    field_id: int
    type: str
    status: str
    date_registered: str
    date_created: str

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

class RemoteTerminalUnitsCreate(RemoteTerminalUnitsBase):
    pass

class SensorsMetersCreate(SensorsMetersBase):
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
