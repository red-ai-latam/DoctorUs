from Config.basics import *
from View.Chat.StartChat import helloWorld,legalInfo


class DoctorUsView:
    """


    """

    def __init__(self):
        pass

    # Start conversation. Ask for legal conditions
    def startChat(self):
        helloWorld()
        return legalInfo()


    # Retrive info from User
    def getProfileInfo(self, dict_questions, id_dict_questions):
        cache = {}
        print(textSeparator)
        print(blankSpace)
        print("Ingrese sus {0}, sin acentos gráficos".format(id_dict_questions))
        print(blankSpace)
        for key in dict_questions:
            cache[key] = input(dict_questions[key])
        return cache

    def getMedicalProfileInfo(self, question, id_dict_questions):
        print(textSeparator)
        print(blankSpace)
        print("Sobre {0}".format(id_dict_questions))
        print(blankSpace)
        answer = input(question)
        if answer == no:
            print(blankSpace)
            return []
        else:
            print(answer.split(" "))
            print(blankSpace)
            return answer.split(" ")

    def getCovidInfo(self):
        self.states[state_gettingCovidInfo].getCOVIDinfo(self.actualUser)
