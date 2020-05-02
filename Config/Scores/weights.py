"""
# Score asociated to each variable. It can be:
# 5 = High importance
# 3 = Medium importance
# 1 = Low importance
# 0 = No importance
"""

# Exposition

# lockdown = "Comuna en cuarentena"
# be_in_touch = "Contacto con paciente COVID"
# travels = " Viajes al extranjero en zonas COVID"


from Config.Questions.userCovidQuestions import *

dict_weights_exposition = {lockdown: 1,
                           travels: 3,
                           be_in_touch: 5}

# Risk

# age = 'Edad'
#
# tbq = 'Fumar'
# oh = 'Alcohol'
# ilegal_drugs = 'Drogas ilícitas'
# urine_state = 'Problemas de micción'
# defecate_state = 'Problemas con defecación'
#
# cx = 'Cirugías'
# hosp = 'Hospitalizaciones en los últimos 3 meses'
# atb = 'Consumo de ATB en los últimos 3 meses'
#
# Se debe indicar que enfermedades, alergias y farmacos se preguntaran, así se puede ponderar cada uno
# ID_ecnt = 'ECNT (enfermedades crónicas)'
# ID_allergies = 'alergias '
# ID_legalDrugs = 'fármacos'


from Config.Questions.userProfileQuestions import *
from Config.Questions.userMedicalProfileQuestions import *

dict_weight_risk = {age: 5,
                    tbq: 1,
                    oh: 1,
                    ID_ecnt: 1}

# Specific Symptoms
#
# fever = "Fiebre sobre 38°C"
# cough = "Tos"
# anosmia = "Anosmia"

from Config.Questions.userSpecSymptoms import *

dict_weight_specSympt = {fever: 5,
                         cough: 3,
                         anosmia: 1
                         }

# Inspecific Symptoms
#
# mialgia = "Mialgia"
# cefalea = "Cefalea"
# escalofrios = "Escalofríos"
# diarrea = "Diarrea"
# odinofagia = "Odinofagia"
# skill_injury = "Lesión en la piel"

from Config.Questions.userInSpecSymptoms import *

dict_weight_inSpecSymp = {mialgia: 1,
                          cefalea: 1,
                          escalofrios: 1,
                          diarrea: 1,
                          odinofagia: 1,
                          skill_injury: 1}
