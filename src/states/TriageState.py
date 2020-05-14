from src.states.BaseState import BaseState, EventData


class TriageState(BaseState):

    def __init__(self, name):
        super().__init__(name=name, on_enter=[self.show_triage_results], on_exit=[self._say_bye])

    def handle(self, event: EventData):
        self.change_state = self._is_bye(event.kwargs["request"]["text"])

    def show_triage_results(self, event: EventData):
        response = event.kwargs["response"]
        user_model = event.kwargs["user_model"]

        text = "Resultados del triage" \
               "" \
               ""
        response.append(text)
        response.append(user_model.call_triage())

    def _is_bye(self, message):
        tokens = [word.lower() for word in message.strip().split()]
        return any(g in tokens
                   for g in ['gracias', 'goodbye', 'chao', 'adios', 'later', 'cya'])

    def _say_bye(self, event: EventData):
        text = "Gracias {0}. Toma las precauciones indicadas!".format(event.kwargs["request"]["user_name"])
        event.kwargs["response"].append(text)
