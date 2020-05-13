from InterviewFlow.states.BaseState import BaseState, EventData
from InterviewFlow.parse import extract_age,extract_keywords,extract_sex
from Utils.Exceptions.CustomExceptions import AmbiguousAnswerException
from Utils.constants import SEX_NORM, MAX_AGE, MIN_AGE

#TODO: arreglar los printeos de excepciones, unificar

class CreateUserState(BaseState):

    def __init__(self, name):
        super().__init__(name=name, on_enter= [self.ask_for_info], on_exit= [self._say_thanks])

    # TODO: Acá serviria algo de NLP, sino cuestionario
    def handle(self, event: EventData):
        """
        Retrive all information needed
        Save to user model

        :param event:
        :return:
        """

        user_model = event.kwargs["user_model"]
        request = event.kwargs["request"]
        response = event.kwargs["response"]

        try:
            age = int(extract_age(request["age"]))
            sex = extract_sex(request["sex"], SEX_NORM)
            if age < MIN_AGE:
                raise ValueError("Ages below 12 are not yet supported.")
            if age > MAX_AGE:
                raise ValueError("Maximum possible age is 130.")
        except (AmbiguousAnswerException, ValueError) as e:
            response.append("Favor repetir tu {0} ".format(e))
        else:
            user_model.set_sex_and_age(sex=sex, age=age)
            self.set_change_state(True)

    def ask_for_info(self, event : EventData):
        #TODO: Adecuar a formato de mensaje
        text = "Favor indicar sexo biologico "
        event.kwargs["response"].append(text)
        text = "Favor indicar edad "
        event.kwargs["response"].append(text)

    def _say_thanks(self, event : EventData):
        text = "Gracias {0}!".format(event.kwargs["request"]["user_name"])
        event.kwargs["response"].append(text)

