from enum import Enum


class ETypeLogEvent(Enum):
    DEBUG = "DEBUG"
    ERROR = "ERROR"
    INFO = "INFO"
    WARNING = "WARNING"
    CRITICAL = "CRITICAL"