from Config.basics import *


def helloWorld():
    print(textSeparator)
    print("Hola a todos")
    print("Bienvenido a DoctorUS")
    print("Este Bot entregará un riesgo de tener COVID19 y los pasos a seguir")
    print("Por favor ingrese los siguientes datos")
    print("Las preguntas de síntomas responda s, para sí")
    print("responda n, para No")
    print("por favor siga las instrucciones")
    print(textSeparator)
    print(blankSpace)
    print(textSeparator)
    print("Ahora le preguntaremos sus antecedentes médicos")
    print("Pero antes")


# TODO: Aca se muestra la información legal, aceptar terminos y condiciones
def legalInfo():
    # Consentimiento Informado#
    print("Por favor leer y firmar si está de acuerdo")
    print("Toda la data se usará de forma anonimizada")
    print("La info no se entregará a terceros sin su autorizacion con fines comerciales")
    print(blankSpace)
    return input("¿Está de acuerdo? ({0}/{1}) ".format(yes, no))
