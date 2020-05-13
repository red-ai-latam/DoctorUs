from InterviewFlow.states.BaseState import BaseState, EventData


class TriageState(BaseState):


    def __init__(self, name):
        super().__init__(name=name, on_exit=[])

    def handle(self, event : EventData):
        pass
