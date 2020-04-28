from Config.basics import kwd_list,yes
from Config.userProfileQuestions import ID_covid, ID_ecnt


class BasicUser(IUser):
    """

    """

    # TODO: Hay que mejorar las preguntas para que sean más inclusivas, tanto si es nacional o extranjero o sexo no binario
    # TODO: En Front, hacer interactiva la manera de responder
    def __init__(self):
        super().__init__()

    def setData(self, ID_dict, key, data):
        if key != kwd_list:
            self.user_info[ID_dict][key] = data
        elif key == kwd_list:
            self.user_info[ID_dict].append(data)

    def calculateProbPreTest(self):
        #TODO: Revisar estos calculos. Primero, se suman n° enfermedades cronicas con exposicion a COVID
        count = len(self.user_info[ID_ecnt]) + self.user_info[ID_covid].count(yes)


