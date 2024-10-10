__version__='1.0.0'
__author__=['Ioannis Tsakmakis']
__date_created__='2023-10-20'
__last_updated__='2024-10-02'

import traceback, inspect
from sqlalchemy.orm import Session
from .engine import SessionLocal
from functools import wraps
from .logger import alchemy, influx

def session_handler_add_delete_update(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        db: Session = kwargs.get('db') or SessionLocal()
        try:
            result = func(*args, db=db, **kwargs)
            db.commit()
            alchemy.info(f"{func.__name__} executed successfully")
            return result
        except Exception as e:
            db.rollback()
            alchemy.error(f"Error occurred {func.__name__}: {str(e)}")
            alchemy.error(traceback.format_exc())
            return {"message": "An unexpected error occurred. Please try again later."}
        finally:
            db.close()
    return wrapper

def session_handler_query(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        db: Session = kwargs.get('db') or SessionLocal()
        try:
            result = func(*args, db=db, **kwargs)
            alchemy.info(f"{func.__name__} executed successfully")
            return result
        except Exception as e:
            alchemy.error(f"Error occurred {func.__name__}: {str(e)}")
            alchemy.error(traceback.format_exc())
            return {"message": "An unexpected error occurred. Please try again later."}
        finally:
            db.close()
    return wrapper

def influxdb_error_handler(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            # Try to execute the wrapped function
            return func(*args, **kwargs)
        except Exception as e:
            # Log the exception, traceback and return a structured error response
            influx.error(f"Error in {func.__name__}: {str(e)}")
            influx.error(traceback.format_exc())
            return {"message": f"Error in {func.__name__}: {str(e)}", "status": "error"}
    return wrapper

def validate_int(*param_names):
    """Decorator to validate that a specific parameter is an integer."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Get the function's signature
            sig = inspect.signature(func)
            bound_args = sig.bind_partial(*args, **kwargs).arguments    

            # Check both positional (args) and keyword (kwargs) arguments
            for param_name in param_names:
                # Check if the param is in keyword arguments
                if param_name in bound_args:
                    if not isinstance(bound_args[param_name], int):
                        alchemy.error(f"{param_name} must be an integer")
                        return {"message": "Bad Request", "errors": [f"{param_name} must be an integer"]}
                
                
            # Call the original function if validation passes
            return func(*args, **kwargs)
        return wrapper
    return decorator

def validate_str(*param_names):
    """Decorator to validate that a specific parameter is an integer."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Get the function's signature
            sig = inspect.signature(func)
            bound_args = sig.bind_partial(*args, **kwargs).arguments    

            # Check if the parameter is present and validate its type
            for index, param_name in enumerate(param_names):
                if bound_args.get('kwargs'):
                    if param_name in bound_args['kwargs'] and not isinstance(bound_args['kwargs'][param_name], str):
                        alchemy.error(f"{param_name} must be a string")
                        return {"message": "Bad Request", "errors": [f"{param_name} must be a string"]}
                elif bound_args.get('args'):
                    if not isinstance(bound_args['args'][index], str):
                        alchemy.error(f"{param_name} must be a string")
                        return {"message": "Bad Request", "errors": [f"{param_name} must be a string"]}
                
            # Call the original function if validation passes
            return func(*args, **kwargs)
        return wrapper
    return decorator

def validate_float(*param_names):
    """Decorator to validate that a specific parameter is an integer."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Get the function's signature
            sig = inspect.signature(func)
            bound_args = sig.bind_partial(*args, **kwargs).arguments    

            # Check if the parameter is present and validate its type
            for index, param_name in enumerate(param_names):
                if bound_args.get('kwargs'):
                    if param_name in bound_args['kwargs'] and not isinstance(bound_args['kwargs'][param_name], float):
                        return {"message": "Bad Request", "errors": [f"{param_name} must be float"]}
                elif bound_args.get('args'):
                    if not isinstance(bound_args['args'][index], float):
                        return {"message": "Bad Request", "errors": [f"{param_name} must be float"]}
                
            # Call the original function if validation passes
            return func(*args, **kwargs)
        return wrapper
    return decorator