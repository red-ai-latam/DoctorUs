from .GUI.GUI import *
from Model.DoctorUsModel import DoctorUsModel


class DoctorUsView:
    """

    """

    def __init__(self):
        pass

    # Start conversation. Ask for legal conditions
    def startChat(self):
        return helloWorld() and legalInfo()

    # Ask questions in dict_questions. Return answers as a dict of text
    def getTextAnswers(self, ID_questions, dict_questions):
        event, values = inputTextWindow(ID_questions, dict_questions)
        if event:
            return values
        else:
            raise Exception

    def getBinaryAnswers(self, ID_questions, dict_questions):
        event, values = yesNoWindow(ID_questions, dict_questions)
        if event:
            return values
        else:
            raise Exception

    def getFuzzyAnswers(self, ID_questions, dict_questions):
        event, values = slideBarWindow(ID_questions, dict_questions)
        if event:
            return values
        else:
            raise Exception

    def alertUser(self, ID_alert):
        if ID_alert == ID_URGENCY:
            generalDisplayWindos(URGENCY_ALERT_TEXT)
        elif ID_alert == ID_SPEC_SYMP:
            generalDisplayWindos(SPECIFIC_SYMPTOMS_TEXT_ALERT)
        elif ID_alert == ID_ALERT_RX:
            generalDisplayWindos(ALERT_RX_TEXT)
        elif ID_alert == ID_IN_SPEC_SYMP:
            generalDisplayWindos(INESPECIFIC_SYMPTOMS_ALERT_TEXT)
        elif ID_alert == ID_ALERT_TELEMEDICINE:
            generalDisplayWindos(TELEMEDICINE_ALERT_TEXT)
        elif ID_alert == ID_ALERT_LOWPROB:
            generalDisplayWindos(LOW_PROBABILITY_ALERT_TEXT)
        elif ID_alert == ID_ALERT_PRE_TEST:
            generalDisplayWindos(PRE_TEST_ALERT_TEXT)

    def hasSymptoms(self):
        return generalYesNoWindows(SYMPTOMS_TEXT_QUESTION)

    def printModel(self, model: DoctorUsModel):
        if input("¿Quieres un resumen de la información? ({0}/{1}) ".format(YES, NO)) == YES:

            print("Summary")

            dict_userInfo = model.userModel
            for key in dict_userInfo:

                if isinstance(dict_userInfo[key], dict) and len(dict_userInfo[key].values()) > 0:
                    print(key)

                    for internKey in dict_userInfo[key]:
                        print("{0} : {1}".format(internKey, dict_userInfo[key][internKey]))
                else:
                    print("{0} : {1}".format(key, dict_userInfo[key]))

            print("Puntaje Exposicion : ", model.getExpositionScore())
            print("Puntaje Riesgo : ", model.getRiskScore())
            print("-------------------------")
            print("Puntaje PreTest : ", model.getPreTestScore())
            print("Puntaje Sintomas Especificos : ", model.getSpecSymp())
            print("Puntaje Sintomas Inespecificos : ", model.getInSpecSymp())
            print("--------------------------")
            print("Puntaje Total : ", model.getTotalScore())
