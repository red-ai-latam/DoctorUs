from InterviewFlow.BasicUserModel import BasicUserModel
from InterviewFlow.states import InitState, CreateUserState, DiagnosisState, TriageState
from InterviewFlow.states.BaseState import BaseState
from transitions import Machine
import logging



logging.basicConfig(level=logging.DEBUG)
logging.getLogger('transitions').setLevel(logging.INFO)

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
            InitState.InitState(name= INIT),
            CreateUserState.CreateUserState(name=CREATE),
            DiagnosisState.DiagnosisState(name=DIAGNOSIS),
            TriageState.TriageState(name=TRIAGE)

        ]

        Machine.__init__(self, states=states, initial=INIT, ignore_invalid_triggers=False,
                         send_event=True, auto_transitions=False)
        self.add_ordered_transitions(conditions=[BaseState.static_check_new_state], prepare=[BaseState.static_handle])

    # actual state handle message via trigger
    def handle_message(self, request):
        # New responses for every income message
        self.cache_response = []

        # Trigger to state. Process request and generate responses
        self.next_state(request= request, user_model = self.user_model, response = self.cache_response)

        # Return responses
        return self.cache_response
