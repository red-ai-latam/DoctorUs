from transitions import State
import abc
from transitions.core import EventData


class BaseState(State):
    """

    """

    __metaclass__ = abc.ABCMeta

    def __init__(self, name, on_enter=None, on_exit=None):
        super().__init__(name=name, on_exit=on_exit, on_enter=on_enter)
        self.change_state = False

    # Wrapper to call method in each state. Override it
    # Handle request send by user
    @staticmethod
    def static_handle(event: EventData):
        event.state.handle(event)

    @abc.abstractmethod
    def handle(self, event: EventData):
        pass

    # Wrapper static method
    @staticmethod
    def static_check_new_state(event: EventData):
        return event.state.check_new_state()

    def check_new_state(self):
        return self.change_state

    def set_change_state(self, b):
        self.change_state = b
