from Config.basics import yes, no

# Inspecific symptoms

ID_inspec_symp = 'síntomas inespecíficos'

mialgia = "Mialgia"
cefalea = "Cefalea"
escalofrios = "Escalofríos"
diarrea = "Diarrea"
odinofagia = "Odinofagia"
skill_injury = "Lesión en la piel"

# Questions
dict_inSpecSymptoms_questions = {mialgia: "¿Tiene dolor muscular? ({0}/{1}) ".format(yes, no),
                                 cefalea: "¿Tiene dolor de cabeza)? ({0}/{1}) ".format(yes, no),
                                 escalofrios: "¿Tiene escalofríos? ({0}/{1}) ".format(yes, no),
                                 diarrea: "¿Tiene diarrea? ({0}/{1}) ".format(yes, no),
                                 odinofagia: "¿Tiene dolor al tragar? ({0}/{1}) ".format(yes, no),
                                 skill_injury: "¿Tiene lesiones en la piel? ({0}/{1}) ".format(yes, no)
                                 }
