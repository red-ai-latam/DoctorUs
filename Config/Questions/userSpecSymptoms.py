from Config.basics import yes, no

# Specific symptoms

ID_spec_symp = 'síntomas específicos'

fever = "Fiebre sobre 38°C"
cough = "Tos"
anosmia = "Anosmia"

# Questions
dict_specSymptoms_questions = {fever: "¿Tiene fiebre sobre 38°C? ({0}/{1}) ".format(yes, no),
                               cough: "¿Tiene tos? ({0}/{1}) ".format(yes, no),
                               anosmia: "¿Ha perdido el olfato? ({0}/{1}) ".format(yes, no)
                               }
