__version__='1.3.5'
__authors__=['Ioannis Tsakmakis']
__date_created__='2023-10-20'
__last_updated__='2024-10-17'

# from databases_utils import schemas, models
from databases_utils import models, schemas
from sqlalchemy.orm import Session
from sqlalchemy import text, or_, select, update
from .aws_utils import KeyManagementService
from .decorators import session_handler_add_delete_update, session_handler_query, validate_int, validate_str, validate_float

class User:

    @staticmethod
    @session_handler_add_delete_update
    def add(user: schemas.UsersTableCreate, db: Session = None):
        new_user = models.Users(name=user.name, email=user.email, account_type=user.account_type, subscription_expires_in=user.subscription_expires_in)
        db.add(new_user)

    @staticmethod
    @validate_str('name')
    @session_handler_query
    def get_by_name(name: str, db: Session = None):
        return db.execute(select(models.Users).filter_by(name=name)).one_or_none()

    @staticmethod
    @validate_int('id')
    @session_handler_query
    def get_by_id(id: int, db: Session = None):
        return db.execute(select(models.Users).filter_by(id=id)).one_or_none()

    @staticmethod
    @validate_str('email')
    @session_handler_query
    def get_by_email(email: str, db: Session = None):
        return db.execute(select(models.Users).filter_by(email=email)).one_or_none()

    @staticmethod
    @validate_str('name')
    @session_handler_add_delete_update
    def delete_by_name(name: str, db: Session = None):
            result = db.execute(select(models.Users).filter_by(name=name)).one_or_none()
            if result is not None:
                db.delete(result.Users)
            else:
                return {"message": "Not Found", "errors": ["The provided name does not exist in the users table"]}, 404

class Stations:

    @staticmethod
    @session_handler_add_delete_update
    def add(station: schemas.StationsCreate, db: Session = None):
        new_station = models.Stations(brand=station.brand, model=station.model, code=station.code, date_created=station.date_created,
                                    last_communication=station.last_communication, status=station.status, longitude=station.longitude,
                                    latitude=station.latitude, elevation=station.elevation, access=station.access, name=station.name, icon_type=station.icon_type)
        db.add(new_station)

    @staticmethod
    @validate_int('id')
    @session_handler_query
    def get_by_id(id: int, db: Session = None):
        return db.execute(select(models.Stations).filter_by(id = id)).one_or_none()

    @staticmethod
    @validate_str('code')
    @session_handler_query
    def get_by_code(code: str, db: Session = None):
        return db.execute(select(models.Stations).filter_by(code = code)).one_or_none()

    @staticmethod
    @session_handler_query
    @validate_str('brand')
    def get_by_brand(brand: str, db: Session = None):
        return db.execute(select(models.Stations).filter_by(brand = brand)).all()

    @staticmethod
    @validate_int('user_id')
    @session_handler_query
    def get_by_access(user_id: int, db: Session = None):
        return db.execute(select(models.Stations).filter(text("JSON_CONTAINS(JSON_UNQUOTE(JSON_EXTRACT(access, '$.users')), CAST(:user AS JSON), '$')").params(user=user_id))).all() 

    @staticmethod
    @validate_int('station_id')
    @validate_float('new_datetime')
    @session_handler_add_delete_update
    def update_date_created(station_id: int, new_datetime: float, db: Session = None):
        db.execute(update(models.Stations).where(models.Stations.id==station_id).values(date_created=new_datetime))

    @staticmethod
    @validate_int('station_id')
    @validate_float('new_datetime')
    @session_handler_add_delete_update
    def update_last_communication(station_id: int, new_datetime: float, db: Session = None):
        db.execute(update(models.Stations).where(models.Stations.id==station_id).values(last_communication=new_datetime))

    @staticmethod
    @validate_int('station_id')
    @validate_str('current_status')
    @session_handler_add_delete_update
    def update_status(station_id: int, current_status: str, db: Session = None):
        db.execute(update(models.Stations).where(models.Stations.id==station_id).values(status=current_status))

    @staticmethod
    @validate_int('station_id','user_id')
    @session_handler_add_delete_update
    def add_user_to_station(station_id: int, user_id: int, db: Session = None):
        access=db.execute(select(models.Stations).filter_by(id=station_id)).one_or_none()
        if user_id not in access[0].access['users']:
            access[0].access['users'].append(user_id)

    @staticmethod
    @validate_int('station_id','user_id')
    @session_handler_add_delete_update
    def delete_user_from_station(station_id: int, user_id: int, db: Session = None):
        access=db.execute(select(models.Stations).filter_by(id=station_id)).one_or_none()
        if access.Stations:
            if user_id not in access[0].access['users']:
                access[0].access['users'].remove(user_id)

    @staticmethod
    @validate_str('code')
    @session_handler_add_delete_update
    def delete_by_code(code: str, db: Session = None):
        result = db.execute(select(models.Stations).filter_by(code = code)).one_or_none()
        if result is not None:
            db.delete(result.Stations)
        else:
            return {"message": "Not Found", "errors": ["The provided code does not exist in the stations table"]}, 404

class Gateways:

    @staticmethod
    @session_handler_add_delete_update
    def add(gateway: schemas.GatewaysCreate, db: Session = None):
        new_gateway = models.GateWays(brand= gateway.brand, model=gateway.model, code=gateway.code,
                                    name = gateway.name, station_id=gateway.station_id)
        db.add(new_gateway)

    @staticmethod
    @validate_str('code')
    @session_handler_query
    def get_by_code(code: str, db: Session = None):
        return db.execute(select(models.GateWays).filter_by(code=code)).one_or_none()

class ReapeaterUnits:

    @staticmethod
    @session_handler_add_delete_update
    def add(rpu: schemas.ReapeaterUnitsBase, db: Session = None):
        new_rtu = models.RemoteTerminalUnits(brand=rpu.brand, model=rpu.model, code=rpu.code, date_created=rpu.date_created,
                                            last_communication=rpu.last_communication, status=rpu.status, longitude=rpu.longitude,
                                            latitude=rpu.latitude, elevation=rpu.elevation, name=rpu.name,
                                            station_id=rpu.station_id)
        db.add(new_rtu)

    @staticmethod
    @validate_int('id')
    @session_handler_query
    def get_by_id(id: str, db: Session = None):
        return db.execute(select(models.RepeaterUnits).filter_by(id = id)).one_or_none()

    @staticmethod
    @validate_str('code')
    @session_handler_query
    def get_by_code(code: str, db: Session = None):
        return db.execute(select(models.RepeaterUnits).filter_by(code = code)).one_or_none()

    @staticmethod
    @validate_int('station_id')
    @session_handler_query
    def get_by_station_id(station_id: int, db: Session = None):
        return db.execute(select(models.RepeaterUnits).filter_by(station_id=station_id)).one_or_none()
    
    @staticmethod
    @validate_int('repeater_id')
    @validate_float('new_datetime')
    @session_handler_add_delete_update
    def update_date_created(repeater_id: int, new_datetime: float, db: Session = None):
        db.execute(update(models.RepeaterUnits).where(models.RepeaterUnits.id==repeater_id).values(date_created=new_datetime))

    @staticmethod
    @validate_int('repeater_id')
    @validate_float('new_datetime')
    @session_handler_add_delete_update
    def update_last_communication(repeater_id: int, new_datetime: float, db: Session = None):
        db.execute(update(models.RepeaterUnits).where(models.RepeaterUnits.id==repeater_id).values(last_communication=new_datetime))

    @staticmethod
    @validate_int('repeater_id')
    @validate_str('current_status')
    @session_handler_add_delete_update
    def update_status(repeater_id: int, current_status: str, db: Session = None):
        db.execute(update(models.RepeaterUnits).where(models.RepeaterUnits.id==repeater_id).values(status=current_status))

    @staticmethod
    @validate_str('code')
    @session_handler_add_delete_update
    def delete_by_code(code: str, db: Session = None):
        result = db.execute(select(models.RepeaterUnits).filter_by(code = code)).one_or_none()
        if result is not None:
            db.delete(result.RepeaterUnits)
        else:
            return {"message": "Not Found", "errors": ["The provided code does not exist in the repeater units table"]}, 404

class RemoteTerminalUnits:

    @staticmethod
    @session_handler_add_delete_update
    def add(rtu: schemas.RemoteTerminalUnitsCreate, db: Session = None):
        new_rtu = models.RemoteTerminalUnits(brand=rtu.brand, model=rtu.model, code=rtu.code, date_created=rtu.date_created,
                                            last_communication=rtu.last_communication, status=rtu.status, longitude=rtu.longitude,
                                            latitude=rtu.latitude, elevation=rtu.elevation, name=rtu.name,
                                            station_id=rtu.station_id, repeater_id=rtu.repeater_id)
        db.add(new_rtu)

    @staticmethod
    @validate_int('id')
    @session_handler_query
    def get_by_id(id: str, db: Session = None):
        return db.execute(select(models.RemoteTerminalUnits).filter_by(id = id)).one_or_none()

    @staticmethod
    @validate_str('code')
    @session_handler_query
    def get_by_code(code: str, db: Session = None):
        return db.execute(select(models.RemoteTerminalUnits).filter_by(code = code)).one_or_none()

    @staticmethod
    @validate_int('station_id')
    @session_handler_query
    def get_by_station_id(station_id: int, db: Session = None):
        return db.execute(select(models.RemoteTerminalUnits).filter_by(station_id=station_id)).one_or_none()
    
    @staticmethod
    @validate_int('repeater_id')
    @session_handler_query
    def get_by_repeater_id(repeater_id: int, db: Session = None):
        return db.execute(select(models.RepeaterUnits).filter_by(repeater_id=repeater_id)).one_or_none()

    @staticmethod
    @validate_int('rtu_id')
    @validate_float('new_datetime')
    @session_handler_add_delete_update
    def update_date_created(rtu_id: int, new_datetime: float, db: Session = None):
        db.execute(update(models.RemoteTerminalUnits).where(models.RemoteTerminalUnits.id==rtu_id).values(date_created=new_datetime))

    @staticmethod
    @validate_int('rtu_id')
    @validate_float('new_datetime')
    @session_handler_add_delete_update
    def update_last_communication(rtu_id: int, new_datetime: float, db: Session = None):
        db.execute(update(models.RemoteTerminalUnits).where(models.RemoteTerminalUnits.id==rtu_id).values(last_communication=new_datetime))

    @staticmethod
    @validate_int('rtu_id')
    @validate_str('current_status')
    @session_handler_add_delete_update
    def update_status(rtu_id: int, current_status: str, db: Session = None):
        db.execute(update(models.RemoteTerminalUnits).where(models.RemoteTerminalUnits.id==rtu_id).values(status=current_status))

    @staticmethod
    @validate_str('code')
    @session_handler_add_delete_update
    def delete_by_code(code: str, db: Session = None):
        result = db.execute(select(models.RemoteTerminalUnits).filter_by(code = code)).one_or_none()
        if result is not None:
            db.delete(result.RemoteTerminalUnits)
        else:
            return {"message": "Not Found", "errors": ["The provided code does not exist in the remote terminal units table"]}, 404
             
class MonitoredParameters:

    @staticmethod
    @session_handler_add_delete_update
    def add(monitored_parameters: schemas.MonitoredParametersCreate, db: Session = None):
        new_monitored_parameters = models.MonitoredParameters(type=monitored_parameters.device_type, measurement=monitored_parameters.measurement,
                                                            unit=monitored_parameters.unit, date_created=monitored_parameters.date_created,
                                                            latest_communication=monitored_parameters.last_communication,
                                                            status=monitored_parameters.status, device_height=monitored_parameters.device_height, name =monitored_parameters.name,
                                                            code=monitored_parameters.code, station_id=monitored_parameters.station_id, rtu_id=monitored_parameters.rtu_id)
        db.add(new_monitored_parameters)

    @staticmethod
    @validate_int('station_id')
    @session_handler_query
    def get_by_station_id(station_id: int, db: Session = None):

        rtus = db.execute(select(models.RemoteTerminalUnits).filter_by(station_id=station_id)).all()
        if len(rtus) == 0:
            return db.execute(select(models.MonitoredParameters).filter_by(station_id=station_id)).all()
        else:
            return db.execute(select(models.MonitoredParameters).filter(or_(models.MonitoredParameters.station_id==station_id,
                                                                models.MonitoredParameters.rtu_id.in_(rtus.id)))).all()

    @staticmethod
    @validate_int('repeater_id')
    @session_handler_query
    def get_by_repeater_id(repeater_id: int, db: Session = None):
        rtus = db.execute(select(models.RemoteTerminalUnits).filter_by(repeater_id=repeater_id)).one_or_none()
        return db.execute(select(models.MonitoredParameters).filter(models.MonitoredParameters.rtu_id.in_(rtus.id))).all()

    @staticmethod
    @validate_int('id')
    @session_handler_query
    def get_by_id(id: int, db: Session = None):
        return db.execute(select(models.MonitoredParameters).filter_by(id=id)).one_or_none()
    
    @staticmethod
    @validate_int('rtu_id')
    @session_handler_query
    def get_by_rtu_id(rtu_id: int, db: Session = None):
        return db.execute(select(models.MonitoredParameters).filter_by(rtu_id=rtu_id)).all()

    @staticmethod
    @validate_int('monitored_parameter_id')
    @validate_float('new_datetime')
    @session_handler_add_delete_update
    def update_last_communication(monitored_parameter_id: int, new_datetime: float, db: Session = None):
        db.execute(update(models.MonitoredParameters).where(models.MonitoredParameters.id==monitored_parameter_id).values(last_communication=new_datetime))

    @staticmethod
    @validate_int('monitored_parameter_id')
    @validate_str('current_status')
    @session_handler_add_delete_update
    def update_status(monitored_parameter_id: int, current_status: str, db: Session = None):
        db.execute(update(models.MonitoredParameters).where(models.MonitoredParameters.id==monitored_parameter_id).values(status=current_status))

    @staticmethod
    @validate_int('station_id')
    @validate_str('current_status')
    @session_handler_add_delete_update
    def update_status_by_station_id(station_id: int, current_status: str, db: Session = None):
        db.execute(update(models.MonitoredParameters).where(models.MonitoredParameters.station_id==station_id).values(status=current_status))

    @staticmethod
    @validate_str('code')
    @session_handler_add_delete_update
    def delete_by_code(code: str, db: Session = None):
        result = db.execute(select(models.MonitoredParameters).filter_by(code = code)).one_or_none()
        if result is not None:
            db.delete(result.MonitoredParameters)
        else:
            return {"message": "Not Found", "errors": ["The provided MonitoredParameter code does not exist"]}, 404

class DavisApiCredentials:

    @staticmethod
    @session_handler_add_delete_update
    def add(api_cred: schemas.DavisApiCredentialsCreate, db: Session = None):
        encrypt_key_id = KeyManagementService().encrypt_data(unencrypted_text=api_cred.key_id, key_id=api_cred.key_id)
        encrypt_secrete_name = KeyManagementService().encrypt_data(unencrypted_text=api_cred.secret_name, key_id=api_cred.key_id)
        new_api_cred = models.DavisApiCredentials(station_id=api_cred.station_id, key_id=encrypt_key_id, secret_name=encrypt_secrete_name)
        db.add(new_api_cred)

    @staticmethod
    @validate_int('station_id')
    @session_handler_query
    def get_by_station_id(station_id: int, db: Session = None):
        return db.execute(select(models.DavisApiCredentials).filter_by(station_id=station_id)).one_or_none()

    @staticmethod
    @validate_int('station_id')
    @validate_str('new_key_id')
    @session_handler_add_delete_update
    def update_key_id_by_station_id(station_id: int, new_key_id: str, db: Session = None):
        db.execute(update(models.DavisApiCredentials).where(models.DavisApiCredentials.station_id==station_id).values(key_id=new_key_id))

    @staticmethod
    @validate_int('station_id')
    @validate_str('new_secret_name')
    @session_handler_add_delete_update
    def update_secret_name_by_station_id(station_id: int, new_secret_name: str, db: Session = None):
        db.execute(update(models.DavisApiCredentials).where(models.DavisApiCredentials.station_id==station_id).values(secret_name=new_secret_name))

    @staticmethod
    @validate_int('station_id')
    @session_handler_add_delete_update
    def delete_by_station_id(station_id: int, db: Session = None):
        result = db.execute(select(models.DavisApiCredentials).filter_by(station_id=station_id)).one_or_none()
        if result is not None:
            db.delete(result.DavisApiCredentials)
        else:
            return {"message": "Not Found", "errors": ["The provided station is does not exist"]}, 404
        
class MetricaApiCredentials:

    @staticmethod
    @session_handler_add_delete_update
    def add(api_cred: schemas.MetricaApiCredentialsCreate, db: Session = None):
        encrypt_key_id = KeyManagementService().encrypt_data(unencrypted_text=api_cred.key_id, key_id=api_cred.key_id)
        encrypt_secrete_name = KeyManagementService().encrypt_data(unencrypted_text=api_cred.secret_name, key_id=api_cred.key_id)
        new_api_cred = models.MetricaApiCredentials(station_id=api_cred.station_id, key_id=encrypt_key_id, secret_name=encrypt_secrete_name)
        db.add(new_api_cred)

    @staticmethod
    @validate_int('station_id')
    @session_handler_query
    def get_by_station_id(station_id: int, db: Session = None):
        return db.execute(select(models.MetricaApiCredentials).filter_by(station_id=station_id)).one_or_none()

    @staticmethod
    @validate_int('station_id')
    @validate_str('new_key_id')
    @session_handler_add_delete_update
    def update_key_id_by_station_id(station_id: int, new_key_id: str, db: Session = None):
        db.execute(update(models.MetricaApiCredentials).where(models.MetricaApiCredentials.station_id==station_id).values(key_id=new_key_id))

    @staticmethod
    @validate_int('station_id')
    @validate_str('new_secret_name')
    @session_handler_add_delete_update
    def update_secret_name_by_station_id(station_id: int, new_secret_name: str, db: Session = None):
        db.execute(update(models.MetricaApiCredentials).where(models.MetricaApiCredentials.station_id==station_id).values(secret_name=new_secret_name))

    @staticmethod
    @validate_int('station_id')
    @session_handler_add_delete_update
    def delete_by_station_id(station_id: int, db: Session = None):
        result = db.execute(select(models.MetricaApiCredentials).filter_by(station_id=station_id)).one_or_none()
        if result is not None:
            db.delete(result.MetricaApiCredentials)
        else:
            return {"message": "Not Found", "errors": ["The provided station is does not exist"]}, 404
        
class ADCONApiCredentials:

    @staticmethod
    @session_handler_add_delete_update
    def add(api_cred: schemas.ADCONApiCredentialsCreate, db: Session = None):
        encrypt_key_id = KeyManagementService().encrypt_data(unencrypted_text=api_cred.key_id, key_id=api_cred.key_id)
        encrypt_secrete_name = KeyManagementService().encrypt_data(unencrypted_text=api_cred.secret_name, key_id=api_cred.key_id)
        new_api_cred = models.ADCONApiCredentials(station_id=api_cred.station_id, key_id=encrypt_key_id, secret_name=encrypt_secrete_name)
        db.add(new_api_cred)

    @staticmethod
    @validate_int('station_id')
    @session_handler_query
    def get_by_station_id(station_id: int, db: Session = None):
        return db.execute(select(models.ADCONApiCredentials).filter_by(station_id=station_id)).one_or_none()

    @staticmethod
    @validate_int('station_id')
    @validate_str('new_key_id')
    @session_handler_add_delete_update
    def update_key_id_by_station_id(station_id: int, new_key_id: str, db: Session = None):
        db.execute(update(models.ADCONApiCredentials).where(models.ADCONApiCredentials.station_id==station_id).values(key_id=new_key_id))

    @staticmethod
    @validate_int('station_id')
    @validate_str('new_secret_name')
    @session_handler_add_delete_update
    def update_secret_name_by_station_id(station_id: int, new_secret_name: str, db: Session = None):
        db.execute(update(models.ADCONApiCredentials).where(models.ADCONApiCredentials.station_id==station_id).values(secret_name=new_secret_name))

    @staticmethod
    @validate_int('station_id')
    @session_handler_add_delete_update
    def delete_by_station_id(station_id: int, db: Session = None):
        result = db.execute(select(models.ADCONApiCredentials).filter_by(station_id=station_id)).one_or_none()
        if result is not None:
            db.delete(result.ADCONApiCredentials)
        else:
            return {"message": "Not Found", "errors": ["The provided station is does not exist"]}, 404