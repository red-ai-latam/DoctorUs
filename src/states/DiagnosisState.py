from src.states.BaseState import BaseState, EventData
from src.models import BasicUserModel
from src.utils.constants import ANSWER_NORM
from src.utils.parse import extract_decision
from src.utils.exceptions import AmbiguousAnswerException


class DiagnosisState(BaseState):
    """

    """

    def __init__(self, name):
        super().__init__(name=name, on_enter=[self.start_interview], on_exit=[self.no_more_interview])

    # TODO: Parsear previamente respuesta del usuario, asegurar formato
    def handle(self, event: EventData):

        evidence = event.kwargs["request"]["evidence"]
        response = event.kwargs["response"]
        user_model: BasicUserModel = event.kwargs["user_model"]

        if evidence:
            try:
                for ev in evidence:
                    user_model.add_evidence(id=ev["id"], choice=extract_decision(ev["choice_id"], ANSWER_NORM))

                if user_model.should_stop():
                    self.set_change_state(True)
                else:
                    response.append(user_model.call_diagnosis())

            except (AmbiguousAnswerException, ValueError) as e:
                response.append("Favor repetir tu {0} ".format(e))
        else:
            response.append(user_model.get_evidence_questions())

    def start_interview(self, event: EventData):
        """
        Send first round of questions
        :param event:
        :return:
        """
        user_model: BasicUserModel = event.kwargs["user_model"]
        response = event.kwargs["response"]

        text = "Empieza la entrevista !"

        response.append(text)

        diagosis_results = user_model.call_diagnosis()
        response.append(diagosis_results.questions)

    def no_more_interview(self, event : EventData):
        text = " Gracias por la información! " \
               " Hemos recopilado la suficiente información. " \
               "A continuación se mostrarán tus resultados :" \
               "" \
               ""
        event.kwargs["response"].append(text)
