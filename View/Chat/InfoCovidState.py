from Config.basics import *
from Config.userProfileQuestions import dict_covid_questions, ID_covid
from Model import IUser

class InfoCovidState:
    """


    """

    def __init__(self):
        pass

    # Get Covid info about exposition to it
    def getCOVIDinfo(self, actualUser : IUser.IUser):
        print(textSeparator)
        print(blankSpace)
        print("Le preguntaremos por su exposición al COVID")
        print(blankSpace)
        for key in dict_covid_questions:
            answer = input(dict_covid_questions[key])
            actualUser.setData(ID_covid, key, answer)

        actualUser.calculateProbPreTest()
        print(blankSpace)
        print("Conteo pre-test es igual a {0}".format(actualUser.getProbPreTest()))
