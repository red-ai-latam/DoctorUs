from src.models.BasicUserModel import BasicUserModel
from src.states import InitState, CreateUserState, DiagnosisState, TriageState
from src.states.BaseState import BaseState
from transitions import Machine
import logging

logging.basicConfig(level=logging.DEBUG)
logging.getLogger('transitions').setLevel(logging.DEBUG)

# Define states
INIT = "init"
CREATE = "create"
RISK_FACTOR = "risk factor"
DIAGNOSIS = "diagnosis"
TRIAGE = "triage"


class CovidFlow(Machine):
    """

    """

    def __init__(self):
        self.user_model = BasicUserModel(api_model="infermedica-es-xl", api_version='covid19')

        # To store response from model to user.
        self.cache_response = []

        states = [
            InitState.InitState(name=INIT),
            CreateUserState.CreateUserState(name=CREATE),
            DiagnosisState.DiagnosisState(name=DIAGNOSIS),
            TriageState.TriageState(name=TRIAGE)
        ]

        Machine.__init__(self, states=states, initial=INIT, ignore_invalid_triggers=False,
                         send_event=True, auto_transitions=False)
        self.add_ordered_transitions(conditions=[BaseState.static_check_new_state], prepare=[BaseState.static_handle])

    def handle_message(self, request):
        """
        Send a trigger to actual state to handle income message.
        Process request and generate a list of response

        :param request:
        :return: a list of responses
        """

        self.cache_response = []
        self.next_state(request=request, user_model=self.user_model, response=self.cache_response)
        return self.cache_response

    def reset(self):
        self.user_model.reset_model()
        for key, value in self.states.items():
            value.reset_data()
