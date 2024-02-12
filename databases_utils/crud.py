__version__='1.2.0'
__authors__=['Ioannis Tsakmakis']
__date_created__='2023-10-20'
__last_updated__='2024-02-12'

from databases_utils import schemas, models
from databases_utils.engine import SessionLocal, logging_path
from sqlalchemy.orm import Session
from sqlalchemy import text, or_, select, event
from datetime import datetime
import logging

# Configure the logger
logging.basicConfig(filename=f'{logging_path}/sqlalchemy_connection.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger('sqlalchemy')

# Function to log SQLAlchemy session events
def log_sqlalchemy_session_events(session, flush_context, instances):
    for obj in session.new.union(session.dirty).union(session.deleted):
        logger.info(f"\nSession - Statement executed - {datetime.now().isoformat()}: {obj}\n")

class User:

    @staticmethod
    def add(user: schemas.UsersTableCreate, db: Session = SessionLocal()):
        event.listen(db, 'before_flush', log_sqlalchemy_session_events)
        new_user = models.Users(name=user.name, email=user.email, subscription_expires_in=user.subscription_expires_in)
        db.add(new_user)
        db.commit()       

    @staticmethod
    def get_by_name(name: str, db: Session = SessionLocal()):
        event.listen(db, 'before_flush', log_sqlalchemy_session_events)
        return db.execute(select(models.Users).filter_by(name=name)).one_or_none()

    @staticmethod
    def get_by_id(id: int, db: Session = SessionLocal()):
        event.listen(db, 'before_flush', log_sqlalchemy_session_events)
        return db.execute(select(models.Users).filter_by(id=id)).one_or_none()
    
    @staticmethod
    def get_by_email(email: str, db: Session = SessionLocal()):
        event.listen(db, 'before_flush', log_sqlalchemy_session_events)
        return db.execute(select(models.Users).filter_by(email=email)).one_or_none()

class Stations:

    @staticmethod
    def add(station: schemas.StationsCreate, db: Session = SessionLocal()):
        event.listen(db, 'before_flush', log_sqlalchemy_session_events)
        new_station = models.Stations(brand=station.brand, model=station.model, code=station.code, date_created=station.date_created,
                                      last_communication=station.last_communication, status=station.status, longitude=station.longitude,
                                      latitude=station.latitude, elevation=station.elevation, access=station.access, name=station.name, icon_type=station.icon_type)
        db.add(new_station)
        db.commit()

    @staticmethod
    def get_by_id(id: int, db: Session = SessionLocal()):
        event.listen(db, 'before_flush', log_sqlalchemy_session_events)
        return db.execute(select(models.Stations).filter_by(id = id)).one_or_none()

    @staticmethod
    def get_by_code(code: str, db: Session = SessionLocal()):
        event.listen(db, 'before_flush', log_sqlalchemy_session_events)
        return db.execute(select(models.Stations).filter_by(code = code)).one_or_none()

    @staticmethod
    def get_by_brand(brand: str, db: Session = SessionLocal()):
        event.listen(db, 'before_flush', log_sqlalchemy_session_events)
        return db.execute(select(models.Stations).filter_by(brand = brand)).all()
    
    @staticmethod
    def get_by_access(user_id: int, db: Session = SessionLocal()):
        event.listen(db, 'before_flush', log_sqlalchemy_session_events)
        return db.execute(select(models.Stations).filter(text("JSON_CONTAINS(JSON_UNQUOTE(JSON_EXTRACT(access, '$.users')), CAST(:user AS JSON), '$')").params(user=user_id))).all() 
    
    @staticmethod
    def update_date_created(station_id: int, new_datetime: str, db: Session = SessionLocal()):
        event.listen(db, 'before_flush', log_sqlalchemy_session_events)
        station=db.execute(select(models.Stations).filter_by(id=station_id)).one_or_none()
        if station.Stations:
            station.Stations.date_created=new_datetime
            db.commit()
        else:
            db.close()

    @staticmethod
    def update_last_communication(station_id: int, new_datetime: str, db: Session = SessionLocal()):
        event.listen(db, 'before_flush', log_sqlalchemy_session_events)
        station=db.execute(select(models.Stations).filter_by(id=station_id)).one_or_none()
        if station.Stations:
            station.Stations.last_communication=new_datetime
            db.commit()
        else:
            db.close()

    @staticmethod
    def update_status(station_id: int, current_status: str, db: Session = SessionLocal()):
        event.listen(db, 'before_flush', log_sqlalchemy_session_events)
        station=db.execute(select(models.Stations).filter_by(id=station_id)).one_or_none()
        if station.Stations:
            station.Stations.status=current_status
            db.commit()
        else:
            db.close()

    @staticmethod
    def delete_by_code(code: str, db: Session = SessionLocal()):
        event.listen(db, 'before_flush', log_sqlalchemy_session_events)
        result = db.execute(select(models.Stations).filter_by(code = code)).one_or_none()
        if result.Stations:
            db.delete(result.Stations)
        else: db.close()

class Gateways:

    @staticmethod
    def add(gateway: schemas.GatewaysCreate, db: Session = SessionLocal()):
        event.listen(db, 'before_flush', log_sqlalchemy_session_events)
        new_gateway = models.GateWays(brand= gateway.brand, model=gateway.model, code=gateway.code,
                                      name = gateway.name, station_id=gateway.station_id)
        db.add(new_gateway)
        db.commit()

    @staticmethod
    def get_by_code(code: str, db: Session = SessionLocal()):
        event.listen(db, 'before_flush', log_sqlalchemy_session_events)
        return db.execute(select(models.GateWays).filter_by(code=code)).one_or_none()

class ReapeaterUnits:

    @staticmethod
    def add(rpu: schemas.ReapeaterUnitsBase, db: Session = SessionLocal()):
        event.listen(db, 'before_flush', log_sqlalchemy_session_events)
        new_rtu = models.RemoteTerminalUnits(brand=rpu.brand, model=rpu.model, code=rpu.code, date_created=rpu.date_created,
                                             last_communication=rpu.last_communication, status=rpu.status, longitude=rpu.longitude,
                                             latitude=rpu.latitude, elevation=rpu.elevation, name=rpu.name,
                                             station_id=rpu.station_id)
        db.add(new_rtu)
        db.commit()

    @staticmethod
    def get_by_id(id: str, db: Session = SessionLocal()):
        event.listen(db, 'before_flush', log_sqlalchemy_session_events)
        return db.execute(select(models.RepeaterUnits).filter_by(id = id)).one_or_none()

    @staticmethod
    def get_by_code(code: str, db: Session = SessionLocal()):
        event.listen(db, 'before_flush', log_sqlalchemy_session_events)
        return db.execute(select(models.RepeaterUnits).filter_by(code = code)).one_or_none()
    
    @staticmethod
    def get_by_station_id(station_id: int, db: Session = SessionLocal()):
        event.listen(db, 'before_flush', log_sqlalchemy_session_events)
        return db.execute(select(models.RepeaterUnits).filter_by(station_id=station_id)).one_or_none()
    
    @staticmethod
    def update_date_created(repeater_id: int, new_datetime: str, db: Session = SessionLocal()):
        event.listen(db, 'before_flush', log_sqlalchemy_session_events)
        repeater=db.execute(select(models.RepeaterUnits).filter_by(id=repeater_id)).one_or_none()
        if repeater.RepeaterUnits:
            repeater.RepeaterUnits.date_created=new_datetime
            db.commit()
        else:
            db.close()

    @staticmethod
    def update_last_communication(repeater_id: int, new_datetime: str, db: Session = SessionLocal()):
        event.listen(db, 'before_flush', log_sqlalchemy_session_events)
        repeater=db.execute(select(models.RepeaterUnits).filter_by(id=repeater_id)).one_or_none()
        if repeater.RepeaterUnits:
            repeater.RepeaterUnits.last_communication=new_datetime
            db.commit()
        else:
            db.close()

    @staticmethod
    def update_status(repeater_id: int, current_status: str, db: Session = SessionLocal()):
        event.listen(db, 'before_flush', log_sqlalchemy_session_events)
        repeater=db.execute(select(models.RepeaterUnits).filter_by(id=repeater_id)).one_or_none()
        if repeater.RepeaterUnits:
            repeater.RepeaterUnits.status=current_status
            db.commit()
        else:
            db.close()

    @staticmethod
    def delete_by_code(code: str, db: Session = SessionLocal()):
        event.listen(db, 'before_flush', log_sqlalchemy_session_events)
        result = db.execute(select(models.RepeaterUnits).filter_by(code = code)).one_or_none()
        if result.RepeaterUnits:
            db.delete(result.RepeaterUnits)
        else: db.close()

class RemoteTerminalUnits:

    @staticmethod
    def add(rtu: schemas.RemoteTerminalUnitsCreate, db: Session = SessionLocal()):
        event.listen(db, 'before_flush', log_sqlalchemy_session_events)
        new_rtu = models.RemoteTerminalUnits(brand=rtu.brand, model=rtu.model, code=rtu.code, date_created=rtu.date_created,
                                             last_communication=rtu.last_communication, status=rtu.status, longitude=rtu.longitude,
                                             latitude=rtu.latitude, elevation=rtu.elevation, name=rtu.name,
                                             station_id=rtu.station_id, repeater_id=rtu.repeater_id)
        db.add(new_rtu)
        db.commit()

    @staticmethod
    def get_by_id(id: str, db: Session = SessionLocal()):
        event.listen(db, 'before_flush', log_sqlalchemy_session_events)
        return db.execute(select(models.RemoteTerminalUnits).filter_by(id = id)).one_or_none()

    @staticmethod
    def get_by_code(code: str, db: Session = SessionLocal()):
        event.listen(db, 'before_flush', log_sqlalchemy_session_events)
        return db.execute(select(models.RemoteTerminalUnits).filter_by(code = code)).one_or_none()
    
    @staticmethod
    def get_by_station_id(station_id: int, db: Session = SessionLocal()):
        event.listen(db, 'before_flush', log_sqlalchemy_session_events)
        return db.execute(select(models.RemoteTerminalUnits).filter_by(station_id=station_id)).one_or_none()
    
    @staticmethod
    def get_by_repeater_id(repeater_id: int, db: Session = SessionLocal()):
        event.listen(db, 'before_flush', log_sqlalchemy_session_events)
        return db.execute(select(models.RepeaterUnits).filter_by(repeater_id=repeater_id)).one_or_none()
    
    @staticmethod
    def update_date_created(rtu_id: int, new_datetime: str, db: Session = SessionLocal()):
        event.listen(db, 'before_flush', log_sqlalchemy_session_events)
        rtu=db.execute(select(models.RemoteTerminalUnits).filter_by(id=rtu_id)).one_or_none()
        if rtu.RemoteTerminalUnits:
            rtu.RemoteTerminalUnits.date_created=new_datetime
            db.commit()
        else:
            db.close()

    @staticmethod
    def update_last_communication(rtu_id: int, new_datetime: str, db: Session = SessionLocal()):
        event.listen(db, 'before_flush', log_sqlalchemy_session_events)
        rtu=db.execute(select(models.RemoteTerminalUnits).filter_by(id=rtu_id)).one_or_none()
        if rtu.RemoteTerminalUnits:
            rtu.RemoteTerminalUnits.last_communication=new_datetime
            db.commit()
        else:
            db.close()

    @staticmethod
    def update_status(rtu_id: int, current_status: str, db: Session = SessionLocal()):
        event.listen(db, 'before_flush', log_sqlalchemy_session_events)
        rtu=db.execute(select(models.RemoteTerminalUnits).filter_by(id=rtu_id)).one_or_none()
        if rtu.RemoteTerminaUnits:
            rtu.RemoteTerminalUnits.status=current_status
            db.commit()
        else:
            db.close()

    @staticmethod
    def delete_by_code(code: str, db: Session = SessionLocal()):
        event.listen(db, 'before_flush', log_sqlalchemy_session_events)
        result = db.execute(select(models.RemoteTerminalUnits).filter_by(code = code)).one_or_none()
        if result.RemoteTerminalUnits:
            db.delete(result.RemoteTerminalUnits)
        else: db.close()
    
class MonitoredParameters:

    @staticmethod
    def add(monitored_parameters: schemas.MonitoredParametersCreate, db: Session = SessionLocal()):
        event.listen(db, 'before_flush', log_sqlalchemy_session_events)
        new_monitored_parameters = models.MonitoredParameters(type=monitored_parameters.device_type, measurement=monitored_parameters.measurement,
                                                              unit=monitored_parameters.unit, latest_communication=monitored_parameters.last_communication,
                                                              status=monitored_parameters.status, device_height=monitored_parameters.device_height, name =monitored_parameters.name,
                                                              code=monitored_parameters.code, station_id=monitored_parameters.station_id, rtu_id=monitored_parameters.rtu_id)
        db.add(new_monitored_parameters)
        db.commit()

    @staticmethod
    def get_by_station_id(station_id: int, db: Session = SessionLocal()):
        event.listen(db, 'before_flush', log_sqlalchemy_session_events)
        rtus = db.execute(select(models.RemoteTerminalUnits).filter_by(station_id=station_id)).all()
        if len(rtus) == 0:
            return db.execute(select(models.MonitoredParameters).filter_by(station_id=station_id)).all()
        else:
            return db.execute(select(models.MonitoredParameters).filter(or_(models.MonitoredParameters.station_id==station_id,
                                                            models.MonitoredParameters.rtu_id.in_(rtus.id)))).all()
        
    @staticmethod
    def get_by_repeater_id(repeater_id: int, db: Session = SessionLocal()):
        event.listen(db, 'before_flush', log_sqlalchemy_session_events)
        rtus = db.execute(select(models.RemoteTerminalUnits).filter_by(repeater_id=repeater_id)).one_or_none()
        return db.execute(select(models.MonitoredParameters).filter(models.MonitoredParameters.rtu_id.in_(rtus.id))).all()

    @staticmethod
    def get_by_id(id: int, db: Session = SessionLocal()):
        event.listen(db, 'before_flush', log_sqlalchemy_session_events)
        return db.execute(select(models.MonitoredParameters).filter_by(id=id)).one_or_none()
        
    @staticmethod
    def get_by_rtu_id(rtu_id: int, db: Session = SessionLocal()):
        event.listen(db, 'before_flush', log_sqlalchemy_session_events)
        return db.execute(select(models.MonitoredParameters).filter_by(rtu_id=rtu_id)).all()
    
    @staticmethod
    def update_last_communication(monitored_parameter_id: int, new_datetime: str, db: Session = SessionLocal()):
        event.listen(db, 'before_flush', log_sqlalchemy_session_events)
        monitored_parameter=db.execute(select(models.MonitoredParameters).filter_by(id=monitored_parameter_id)).one_or_none()
        if monitored_parameter.MonitoredParameters:
            monitored_parameter.MonitoredParameters.last_communication=new_datetime
            db.commit()
        else:
            db.close()

    @staticmethod
    def update_status(monitored_parameter_id: int, current_status: str, db: Session = SessionLocal()):
        event.listen(db, 'before_flush', log_sqlalchemy_session_events)
        monitored_parameter=db.execute(select(models.MonitoredParameters).filter_by(id=monitored_parameter_id)).one_or_none()
        if monitored_parameter.MonitoredParameters:
            monitored_parameter.MonitoredParameters.status=current_status
            db.commit()
        else:
            db.close()

    @staticmethod
    def delete_by_code(code: str, db: Session = SessionLocal()):
        event.listen(db, 'before_flush', log_sqlalchemy_session_events)
        result = db.execute(select(models.MonitoredParameters).filter_by(code = code)).one_or_none()
        if result.MonitoredParameters:
            db.delete(result.MonitoredParameters)
        else: db.close()