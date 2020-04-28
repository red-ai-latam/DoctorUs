from Config.basics import *
from Config.userProfileQuestions import *



# TODO: Refactorizar los 3 siguientes métodos, hacen cosas parecidas

# ECNT
# TODO: Correlacion entre estas enfermedades y covid?
# TODO: Por ahora se guarda en arreglos, pero deberia ser diccionario, en donde nosotros mostremos las posibles ECNT
def getECNT(self, actualUser: IUser.IUser):
    print(textSeparator)
    print(blankSpace)
    if input("Tiene enfermedades crónicas ? ({0}/{1}) ".format(yes, no)) == yes:
        print(blankSpace)
        while True:
            answer = input("Que enfermedad crónica tiene? ")
            actualUser.setData(ID_ecnt, kwd_list, answer)
            if input("Alguna más ? ({0}/{1}) ".format(yes, no)) == no:
                print(actualUser.printDict(ID_ecnt))
                break
    else:
        print(blankSpace)
        pass


# Get allergies
# TODO: Por ahora se guarda en arreglos, pero deberia ser diccionario, en donde nosotros mostremos las posibles alergias
def getAllergies(self, actualUser: IUser.IUser):
    self.allergy = []
    print(textSeparator)
    print(blankSpace)
    if input("Tiene alergias ? ({0}/{1}) ".format(yes, no)) == yes:
        print(blankSpace)
        while True:
            answer = input("Que alergia tiene? ")
            actualUser.setData(ID_allergies, kwd_list, answer)
            if input("Alguna más ? ({0}/{1}) ".format(yes, no)) == no:
                print(actualUser.printDict(ID_allergies))
                break
    else:
        print(blankSpace)
        pass


# Get legal drugs
# TODO: Por ahora se guarda en arreglos, pero deberia ser diccionario, en donde nosotros mostremos los posibles farmacos
def getDrugs(self, actualUser: IUser.IUser):
    self.drugs = []
    print(textSeparator)
    print(blankSpace)
    if input("Toma algún fármaco ? ({0}/{1}) ".format(yes, no)) == yes:
        print(blankSpace)
        while True:
            answer = input("Que fármaco toma ? ")
            actualUser.setData(ID_legalDrugs, kwd_list, answer)
            if input("Alguna más ? ({0}/{1}) ".format(yes, no)) == no:
                print(actualUser.printDict(ID_legalDrugs))
                break
    else:
        print(blankSpace)
        pass
