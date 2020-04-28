from Config.basics import yes, no

# Symptoms that requires immediate treatment

ID_urgency = 'sintomas de riesgo vital'

chest_pain = "Dolor torácico"
disnea = "Disnea"
conscience = "Compromiso de consciencia"
blue = "Coloracion azul de cara y labios"

# Questions
dict_urgency_questions = {chest_pain: "¿Tiene dolor torácico? ({0}/{1}) ".format(yes, no),
                          disnea: "¿Siente ahogo? Indique valor de 0 a 5, siendo 5 serias dificultades de respirar ".format(
                              yes, no),
                          conscience: "¿Tiene compromiso de consciencia? ({0}/{1}) ".format(yes, no),
                          blue: "¿Tiene coloración azul en cara y labios? ({0}/{1}) ".format(yes, no)
                          }
