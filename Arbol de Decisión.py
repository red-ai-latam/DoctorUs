#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 18:27:49 2020

@author: Benjamin
"""

# Counter#
count = 0
print("---------------------------------------------------")
print("Hola a todos")
print("Bienvenido a DoctorUS")
print("Este Bot entregará un riesgo de tener COVID19 y los pasos a seguir")
print("Por favor ingrese los siguientes datos")
print("Las preguntas de síntomas responda s, para sí")
print("responda n, para No")
print("por favor siga las instrucciones")
print("---------------------------------------------------")
print("")
print("---------------------------------------------------")
print("Ahora le preguntaremos sus antecedentes médicos")
print("Pero antes")

# Consentimiento Informado#
print("Por favor leer y firmar si está de acuerdo")
print("Toda la data se usará de forma anonimizada")
print("La info no se entragrá a terceros sin su autorizacion con fines comerciales")

# Módulo de Registro#
# Antecedentes#
print("Ingrese sus antecedentes, sin acentos gráficos")
a = input("Inserte su nombre ")
edad = float(input("Inserte su edad "))
RUT = input("Inserte su RUT ")
matri = input("Cuál es su estado civil ")
c = input("Inserte su sexo ")
d = input("Inserte su comuna ")
prevision = input("Cual es su prevision? ")
sueldo = input("Cual es su ingreso familiar ? ")
familia = input("Cuantos integrantes tiene en su familia ? ")
trabajo = input("En que área trabaja ? ")
contrato = input("Tiene contrato ? ")
empleo = ("Cual es su estado laboral ? ")

# Modulo antecdentes médicos#
# Hábitos#
tbq = input("Usted fuma? ")
oh = input("Usted consume alcohol? ")
drogas = input("Consume alguna droga ilícita ? ")
micción = input("Problemas con la micción? ")
defecación = input("Problemas con defeccacion? ")

# Hospitalizaciones y Cirugías#
cx = input("Se ha sometido a cirugías? ")
hosp = input("Ha estado hospitalizado en los últimos 3 meses? ")
atb = input("Ha tenido consumo de ATB en los ultimos 3 meses ? ")

# ECNT#
# Cada vez que escriba una enfermedad, sumar a la lista#
# Nomeclatura HTA, DM, IH, ERC, ICC, TVP, TEP, CA, TX, VIH, IS, AI#
ecnt = input("Tiene enfermedades crónicas ? ")
list_enf_cron = list(ecnt)
enf_cron = []
while ecnt == "s":
    enf_cron = input("Que enfermedad crónica tiene? ")
    if enf_cron == "n":
        break
print(list(enf_cron))
for i in enf_cron:
    count += 1

# Alergias#
alergias = input("Tiene alguna alergia? ")
alerg1 = list(alergias)
while alergias == "s":
    alerg1 = input("Qué alergias tiene ? ")
    if alerg1 == "n":
        break

# FCOS#
# Nomeclatura LST, MTF, HTZ...#
farmacos = input("Toma algún fármaco ? ")
fcos = list(farmacos)
while farmacos == "s":
    fcos = input("Qué fármaco toma ? ")
    if fcos == "n":
        break
print("---------------------------------------------------")

# Ahora calcularemos el riesgo de exposición a COVID que tiene#
# Modulo Preguntas Exposición#
lock_down = input("Su comuna está en lockdown? ")
contacto = input("Tuvo contacto con un paciente COVID? ")
viajes = input("Tuvo viajes al extranjero con alta prevalencia de COVID? ")

# Clasificador Nº2 de Exposicion#

# Separar y priorizar (1)
if lock_down == "s":
    count += 1
else:
    count += 0
# Priorizar (3)
if contacto == "s":
    count += 1
else:
    count += 0
# prioridad (1)
if viajes == "s":
    count += 1
else:
    count += 0
count_exposicion = count

#

# Clasificador Nº3 de Riesgo#
# (3)
if edad >= 65:
    count += 1
else:
    count -= 1
# separar y cada 1
if tbq == "s":
    count += 1
else:
    count -= 1

# cada uno suma 1
#
if ecnt == "s":
    count += 1
else:
    count += 0
count_riesgo = count

# Probabilidad Pre Test#
probabilidad_pretest_riesgo = float(count_riesgo)
probabilidad_pretest_exp = float(count_exposicion)

# Muestra la probabilidad pre test#
# Esto corresponde al riesgo de exposición y riesgo personal combinados#
print("")
print("---------------------------------------------------")
print("Este es el count pre-test")
print(count)
print("Esta es la probabilidad pre test de tener COVID19")
print(probabilidad_pretest)
print("---------------------------------------------------")
print("")

# Continuar con el prograa#
print(" ")
print("Ahora le preguntaremos por síntomas de riesgo vital")
print(" ")

# Clasificador Nº1 Urgencias#
urg1 = input("tiene Dolor toráxico? ")
urg2 = input("tiene Disnea? ") # Fuzzy mayor a 5
urg3 = input("Tiene compromiso de conciencia ? ")
urg4 = input("Tiene coloración azul de cara y labios ? ")
if urg1 == "s" or urg2 == "s" or urg3 == "s" or urg4 == "s":
    print("Llamar al 131")
    print("Esto es una urgencia vital")
    print("Llamando a sus familiares")

print("---------------------------------------------------")
print("Usted no tiene síntomas de urgencia vital")
print("Continue respondiendo")
print("---------------------------------------------------")

# Modulo de Sintomas-Asintomatico - Clasificador Nº2 #
# Si no tiene sintomas y el riesgo es bajo Educar#
# Si el riesgo es alto y no tiene sintomas Telemedicina#
# Si el riesgo es bajo y tiene sintomas continuar con sint especificos#

sintomas = input("¿Tiene síntomas o no síntomas? ")
if sintomas == "s":
    True
else:
    if probabilidad_pretest > 3:
        print("Su riesgo pre test es alto")
        print("Continue respondiendo")
    else:
        print("Su riesgo es bajo")
        print("Usted no tiene síntomas")
        print("Consulte nuevamente si tiene síntomas")
        print("Acceda al siguiente link educativo")
        exit

print("---------------------------------------------------")
print("Usted tiene síntnomas")
print("Continue respondiendo ")
print("Ahora le preguntaremos por síntnomas específicos")
print("---------------------------------------------------")




#TODO:


# Input Sintomas Específicos#
e = input("tiene Fiebre sobre 38ºC? ")
k = input("tiene Tos ? ")
m = input("tiene Anosmia? ")
print("")
if probabilidad_pretest > 3 and ((e == "s" and k == "s") or (e == "s" and m == "s") or (k == "s" and m == "s")):
    print("Usted tiene síntomas específicos de COVID")
    print("Acudir a urgencias a evaluación")
    print("Tomar RT-PCR")

    # Clasif 3
    if count_riesgo >= 3:
        print("Según el Riesgo Personal calculado recomendamos tomar Rx Y Laboratorio")
    else:
        print("Su médico personalemnte decidirá los test a solicitar")
    exit

# Clasificador Síntomas Específicos#
# Si tiene 1 que no sea disnea ni fiebre. Sintomas Especificos entonces Agendar Hora y tomar PCR #
if e == "s":
    count += 1
else:
    count -= 1
if k == "s":
    count += 1
else:
    count -= 1
count_sint_esp = count

if count_sint_esp <= 1:
    print("---------------------------------------------------")
    print("Usted no tiene síntnomas específicos")
    print("Continue respondiendo ")
    print("Ahora le preguntaremos por síntnomas inespecíficos")
    print("---------------------------------------------------")
else:
    print("Muchas gracias")
    exit

# Input Síntomas Inespecíficos#

g = input("tiene Mialgias? ")
h = input("tiene Cefalea? ")
i = input("tiene Calofríos? ")
j = input("tiene Diarrea? ")
l = input("tiene Odinofagia? ")
n = input("tiene lesiones en la piel? ")

# Clasificador Síntomas Inespecíficos#
# Si no tiene sintomas especificos pregunte por inespecificos#
# Si tiene sintomas inespecificos entonces Telemedicina#
# Si no tiene sintomas inespecificos ni especificos entonces Educación#
if g == "s":
    count += 1
else:
    count -= 1
if h == "s":
    count += 1
else:
    count -= 1
if i == "s":
    count += 1
else:
    count -= 1
if j == "s":
    count += 1
else:
    count -= 1
if l == "s":
    count += 1
else:
    count -= 1
if n == "s":
    count += 1
else:
    count -= 1
count_sintomas_inespecificos = count
if count_sintomas_inespecificos >= 1:
    print("Usted tiene síntomas inespecíficos")

# Clasificador Final#
print("")
print("-----------------------------")
print("This is the final count...down turururu tutututu")
print(count)
print("Esta es la probabilidad post-test de tener COVID")
print("Según sus cálculos le recomendaremos lo más adecuado")
print("Calculando")
print("-----------------------------")

# Recomendacion#
print("")
print("")
print("Usted tiene bajo riesgo pero tiene síntomas inespecíficos")
print("Por lo tanto")
print("Según nuestros cálculos le recomendamos ")
if count >= 10:
    print("Acudir a Urgencias para evaluación")
    print("Usted tiene bastantes síntomas inespecíficos")
    print("Le recomendamos acudir a un servicio de urgencia")
elif count < 10 and count > 3:
    print("Llame a su médico de cabecera")
    print("Solicite hora de Telemedicina")
    print("Usted tiene bajo riesgo, pero tiene sintomas inespecíficos")
    print("Dependiendo de la evaluación de su médico")
    print("Debe hacerse test de RT-PCR")
else:
    print("Usted tiene una baja probabilidad de tener COVID y no tiene síntomas")
    print("Repita el cuestionario si presenta nuevos síntomas")
    print("Lo redireccionaremos a un link educativo")
    print("Allí puede aprender sobre cómo protegerse y proteger a los demás")
print("")
print("Hasta la próxima, recuerde entrar con su usuario y contraseña")
