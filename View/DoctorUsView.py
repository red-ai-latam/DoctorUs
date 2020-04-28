from Config.basics import *
from View.Chat.StartChat import helloWorld, legalInfo


class DoctorUsView:
    """


    """

    def __init__(self):
        pass

    # Start conversation. Ask for legal conditions
    def startChat(self):
        helloWorld()
        return legalInfo()

    # Ask questions in dict_questions. Return answers as a dict (cache)
    def getInfo(self, dict_questions, id_dict_questions):
        cache = {}
        print(textSeparator)
        print(blankSpace)
        print("Le preguntaremos por sus {0} ".format(id_dict_questions))
        print(blankSpace)
        for key in dict_questions:
            cache[key] = input(dict_questions[key])
        return cache

    # Retrive info from ECNT, allergies and legal drugs
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
            print(blankSpace)
            return answer.split(" ")

    def alertEmergency(self):
        print("Llamar al 131")
        print("Esto es una urgencia vital")
        print("Llamando a sus familiares")

    def hasSymptoms(self):
        print(blankSpace)
        print(textSeparator)
        if input("¿Tiene algún sintoma? ({0}/{1}) ".format(yes, no)) == yes:
            return True
        else:
            return False

    def alertPreTest(self):
        print(blankSpace)
        print(textSeparator)
        print("Su riesgo pre test es alto")

    def alertLowProb(self):
        print(blankSpace)
        print(textSeparator)
        print("Usted tiene una baja probabilidad de tener COVID y no tiene síntomas")
        print("Repita el cuestionario si presenta nuevos síntomas")
        print("Lo redireccionaremos a un link educativo")
        print("Allí puede aprender sobre cómo protegerse y proteger a los demás")

    def alertSpecificSymptoms(self):
        print(blankSpace)
        print(textSeparator)
        print("Usted tiene síntomas específicos de COVID")
        print("Acudir a urgencias a evaluación")
        print("Tomar RT-PCR")

    def alertRx(self):
        print(blankSpace)
        print(textSeparator)
        print("Según el riesgo rersonal calculado, recomendamos tomar Rx Y laboratorio")

    def alertInspecificSymptoms(self):
        print(blankSpace)
        print(textSeparator)
        print("Acudir a Urgencias para evaluación")
        print("Usted tiene bastantes síntomas inespecíficos")
        print("Le recomendamos acudir a un servicio de urgencia")

    def alertTelemedicine(self):
        print(blankSpace)
        print(textSeparator)
        print("Llame a su médico de cabecera")
        print("Solicite hora de Telemedicina")
        print("Usted tiene bajo riesgo, pero tiene sintomas inespecíficos")
        print("Dependiendo de la evaluación de su médico")
        print("Debe hacerse test de RT-PCR")

