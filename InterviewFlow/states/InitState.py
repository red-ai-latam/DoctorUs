from InterviewFlow.states.BaseState import BaseState, EventData


class InitState(BaseState):


    def __init__(self, name):
        super().__init__(name=name, on_exit=[self._say_hi])

    def handle(self, event : EventData):
        self.change_state = self._is_hi(event.kwargs["request"]["text"])

    def _is_hi(self, message):
        tokens = [word.lower() for word in message.strip().split()]
        return any(g in tokens
                   for g in ['buen día', 'buen dia', 'hola', 'wena', "buena", "ola"])


    def _say_hi(self, event: EventData):
        text = "Hola {0}! Bienvenid@s a DoctorUS \n\n" \
               "Este bot entregará un riesgo de tener COVID19 \n" \
               "y los pasos a seguir \n" \
               "\n" \
               "Por favor ingrese los datos que se pediran \n" \
               "para crear su perfil \n" \
               "\n" \
               "Siga las instrucciones \n".format(event.kwargs["request"]["user_name"])
        event.kwargs["response"].append(text)
