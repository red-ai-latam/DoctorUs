import sys
import threading
import logging
import traceback

from .ETypeLogEvent import ETypeLogEvent
from .ILogData import ILogData


__all__ = ['logger', 'LoggerEvent']


class ThreadSafeSingleton(type):
    _instances = {}
    _singleton_lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        # double-checked locking pattern (https://en.wikipedia.org/wiki/Double-checked_locking)
        if cls not in cls._instances:
            with cls._singleton_lock:
                if cls not in cls._instances:
                    cls._instances[cls] = super(ThreadSafeSingleton, cls).__call__(*args, **kwargs)
                else:
                    cls._instances[cls].__init__(*args, **kwargs)
        return cls._instances[cls]


class LoggerEvent(object):
    __metaclass__ = ThreadSafeSingleton

    def __init__(self):
        self.listLogListener = []

    @staticmethod
    def basic_config_logging(**kargs):
        logging.basicConfig(**kargs)

    @staticmethod
    def default_console_log(dat: ILogData):
        fun_console = logging.info
        if dat.type == ETypeLogEvent.WARNING:
            fun_console = logging.info
        elif dat.type == ETypeLogEvent.ERROR:
            fun_console = logging.error
        elif dat.type == ETypeLogEvent.DEBUG:
            fun_console = logging.debug

        if dat.description:
            msg = '{}:\t{} | {}'.format(dat.tag, dat.message, dat.description)
        else:
            msg = '{}:\t{}'.format(dat.tag, dat.message)
        fun_console(msg)

    def add_logger_listener(self, log_listener):
        self.listLogListener.append(log_listener)

    def log_event_debug(self, tag: str, msg: str, description: str = ""):
        self.add_event(ETypeLogEvent.DEBUG, tag, msg, description)

    def log_event_error(self, tag: str, msg: str, description: str = ""):
        traceback.print_exception(*sys.exc_info())
        self.add_event(ETypeLogEvent.ERROR, tag, msg, description)

    def log_event_info(self, tag: str, msg: str, description: str = ""):
        self.add_event(ETypeLogEvent.INFO, tag, msg, description)

    def log_event_warning(self, tag: str, msg: str, description: str = ""):
        traceback.print_exception(*sys.exc_info())
        self.add_event(ETypeLogEvent.WARNING, tag, msg, description)

    def log_event_critical(self, tag: str, msg: str, description: str = ""):
        traceback.print_exception(*sys.exc_info())
        self.add_event(ETypeLogEvent.CRITICAL, tag, msg, description)

    def add_event(self, _type: ETypeLogEvent, tag: str, msg: str, description: str = ""):
        dat = ILogData(_type=_type, tag=tag, message=msg, description=description)
        for listener in self.listLogListener:
            listener(dat)


logger = LoggerEvent()