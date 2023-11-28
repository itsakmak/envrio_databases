__version__='1.0.6'
__author__='Ioannis Tsakmakis'
__date_created__='2023-10-20'
__last_updated__='2023-11-28'

import databases_library.schemas as schemas
import databases_library.models as models
from databases_library.engine import SessionLocal
from sqlalchemy.orm import Session
from sqlalchemy import text, or_, select

# User Management

class User:

    @staticmethod
    def add(user: schemas.UsersTableCreate, db: Session = SessionLocal()):
        new_user = models.Users(name=user.name, email=user.email, subscription_expires_in=user.subscription_expires_in)
        db.add(new_user)          

    @staticmethod
    def get_by_name(name: str, db: Session = SessionLocal()):
        return db.execute(select(models.Users).filter_by(name=name)).first()

    @staticmethod
    def get_by_id(id: int, db: Session = SessionLocal()):
        return db.execute(select(models.Users).filter_by(id=id)).first()
    
    @staticmethod
    def get_by_email(email: str, db: Session = SessionLocal()):
            return db.execute(select(models.Users).filter_by(email=email)).first()
class Stations:

    @staticmethod
    def add(station: schemas.StationsCreate, db: Session = SessionLocal()):
        new_station = models.Stations(brand=station.brand, model=station.model, code=station.code, date_created=station.date_created,
                                      longitude=station.longitude, latitude=station.latitude, elevation=station.elevation,
                                      access=station.access, name=station.name, icon_type=station.icon_type)
        db.add(new_station)

    @staticmethod
    def get_by_code(code: str, db: Session = SessionLocal()):
        return db.execute(select(models.Stations).filter_by(code = code)).first

    @staticmethod
    def get_by_brand(brand: str, db: Session = SessionLocal()):
        return db.execute(select(models.Stations).filter_by(brand = brand)).all()
    
    @staticmethod
    def get_by_access(user_id: int, db: Session = SessionLocal()):
        return db.execute(select(models.Stations).filter(text("JSON_CONTAINS(JSON_UNQUOTE(JSON_EXTRACT(access, '$.users')), CAST(:user AS JSON), '$')").params(user=user_id))).all() 
    
    @staticmethod
    def update_date_created(station_id: int, new_datetime: str, db: Session = SessionLocal()):
        station=db.execute(select(models.Stations).filter_by(id=station_id)).first()
        if station is not None:
            station.date_created=new_datetime
        else:
            db.close()

    @staticmethod
    def delete_by_code(code: str, db: Session = SessionLocal()):
        result = db.execute(select(models.Stations).filter_by(code = code)).first()
        if result is not None:
            db.delete(result)
        else: db.close()
class Gateways:

    @staticmethod
    def add(gateway: schemas.GatewaysCreate, db: Session = SessionLocal()):
        new_gateway = models.GateWays(brand= gateway.brand, model=gateway.model, code=gateway.code,
                                      name = gateway.name, station_id=gateway.station_id)
        db.add(new_gateway)

    @staticmethod
    def get_by_code(code: str, db: Session = SessionLocal()):
        return db.execute(select(models.GateWays).filter_by(code=code)).first()
class RemoteTerminalUnits:

    @staticmethod
    def add(rtu: schemas.RemoteTerminalUnitsCreate, db: Session = SessionLocal()):
        new_rtu = models.RemoteTerminalUnits(brand=rtu.brand, model=rtu.model, code=rtu.code, longitude=rtu.longitude,
                                             latitude=rtu.latitude, elevation=rtu.elevation,name=rtu.name, station_id=rtu.station_id)
        db.add(new_rtu)

    @staticmethod
    def get_by_code(code: str, db: Session = SessionLocal()):
        return db.execute(select(models.RemoteTerminalUnits).filter_by(code = code)).first()
    
    @staticmethod
    def get_by_station_id(station_id: int, db: Session = SessionLocal()):
        return db.execure(select(models.RemoteTerminalUnits).filter_by(station_id=station_id)).first()
    
class MonitoredParameters:

    @staticmethod
    def add(monitored_parameters: schemas.MonitoredParametersCreate, db: Session = SessionLocal()):
        new_monitored_parameters = models.MonitoredParameters(type=monitored_parameters.device_type, measurement=monitored_parameters.measurement, unit=monitored_parameters.unit,
                                                device_height=monitored_parameters.device_height, name =monitored_parameters.name,
                                                code=monitored_parameters.code, station_id=monitored_parameters.station_id, rtu_id=monitored_parameters.rtu_id)
        db.add(new_monitored_parameters)

    @staticmethod
    def get_by_station_id(station_id: int, db: Session = SessionLocal()):
        rtus = db.execute(select(models.RemoteTerminalUnits).filter_by(station_id=station_id)).first()
        if rtus is None:
            return db.execute(select(models.MonitoredParameters).filter_by(station_id=station_id)).all()
        else:
            return db.execute(select(models.MonitoredParameters).filter(or_(models.MonitoredParameters.station_id==station_id,
                                                            models.MonitoredParameters.rtu_id.in_(rtus.id)))).all()
    @staticmethod
    def get_by_rtu_id(rtu_id: int, db: Session = SessionLocal()):
        return db.execute(select(models.MonitoredParameters).filter_by(rtu_id=rtu_id)).all()
    
    @staticmethod
    def get_by_station_id_and_rtu_id(station_id: int, rtu_id: int,db: Session = SessionLocal()):
        return db.execute(select(models.MonitoredParameters).filter_by(station_id=station_id,rtu_id=rtu_id)).all()
    
    @staticmethod
    def get_by_id(id: int, db: Session = SessionLocal()):
        return db.execute(select(models.MonitoredParameters).filter_by(id = id)).first()

class MeasurementsTranslations:

    @staticmethod
    def add(translation: schemas.MeasurementTranslationsCreate, db: Session = SessionLocal()):
        new_translation = models.MeasurementTranslations(measurement=translation.measurement, el=translation.el, en=translation.en)
        db.add(new_translation)
    
    @staticmethod
    def get_translation_by_measurement(measurement: str, db: Session = SessionLocal()):
        return db.execute(select(models.MeasurementTranslations).filter_by(measurement=measurement)).first()
                  