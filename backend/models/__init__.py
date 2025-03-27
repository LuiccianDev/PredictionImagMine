
from .user import UserPostgreSQL
from .prediction import PredictionPostgres
from .device import DevicePostgreSQL
from .label import LabelPostgres
from .location import LocationPostgreSQL



__all__ = ["PredictionPostgres", "DevicePostgreSQL", "LabelPostgres", "LocationPostgreSQL", "UserPostgreSQL"]