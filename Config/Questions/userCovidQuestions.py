from Config.basics import yes,no
# Exposition to COVID

ID_covid = 'exposición a COVID'


lockdown = "Comuna en cuarentena"
be_in_touch = "Contacto con paciente COVID"
travels = " Viajes al extranjero en zonas COVID"

# Questions of exposition to COVID
dict_covid_questions = {lockdown: "¿Su comuna está en cuarentena? ({0}/{1}) ".format(yes,no),
                         be_in_touch: "¿Tuvo contacto con un paciente COVID? ({0}/{1}) ".format(yes,no),
                         travels: "¿Tuvo viajes al extranjero con alta prevalencia de COVID? ({0}/{1}) ".format(yes,no)
                         }