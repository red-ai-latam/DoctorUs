from Config.basics import yes,no

# User info

ID_basicInfo = 'antecedentes'

name = 'Nombre'
age = 'Edad'
rut = 'Rut'
legal_state = 'Estado civil'
sex = 'Sexo'
commune = 'Comuna'
medical_insurance = 'Previsión de salud'
salary = 'Ingreso familiar'
n_team_members = 'Numero integrantes en grupo familiar'
job = 'Area trabajo'
job_type = 'Tipo contrato'
job_state = 'Estado laboral'

# Questions to get user info
dict_info_questions = {name: "Ingrese su nombre ",
                       age: "Ingrese su edad ",
                       rut: "Ingrese su rut ",
                       legal_state: "¿Cuál es su estado civil (solter@, comprometid@, casad@, viud@) ",
                       sex: "Ingrese su sexo (M/F) ",
                       commune: "Ingrese su comuna ",
                       medical_insurance: "¿Cual es su prevision? ",
                       salary: "¿Cual es su ingreso familiar ? ",
                       n_team_members: "¿Cuantos integrantes tiene en su familia ? ",
                       job: "¿En que área trabaja ? ",
                       job_type: "¿Tiene contrato ? ",
                       job_state: "¿Cuál es su estado laboral ? "}

"---------------------------------------------------------------------------------------------------------------------"
"---------------------------------------------------------------------------------------------------------------------"
"---------------------------------------------------------------------------------------------------------------------"
"---------------------------------------------------------------------------------------------------------------------"
"---------------------------------------------------------------------------------------------------------------------"
"---------------------------------------------------------------------------------------------------------------------"
"---------------------------------------------------------------------------------------------------------------------"
"---------------------------------------------------------------------------------------------------------------------"

# User habits

ID_habits = 'hábitos'

tbq = 'Fumar'
oh = 'Alcohol'
ilegal_drugs = 'Drogas ilícitas'
urine_state = 'Problemas de micción'
defecate_state = 'Problemas con defecación'

# Questions to get user habits
dict_habits_questions = {tbq: "¿Usted fuma? ({0}/{1}) ".format(yes,no),
                         oh: "¿Usted consume alcohol? ({0}/{1}) ".format(yes,no),
                         ilegal_drugs: "¿Consume alguna droga ilícita ? ({0}/{1}) ".format(yes,no),
                         urine_state: "¿Problemas con la micción? ({0}/{1}) ".format(yes,no),
                         defecate_state: "¿Problemas con defeccacion? ({0}/{1}) ".format(yes,no)
                         }

"---------------------------------------------------------------------------------------------------------------------"
"---------------------------------------------------------------------------------------------------------------------"
"---------------------------------------------------------------------------------------------------------------------"
"---------------------------------------------------------------------------------------------------------------------"
"---------------------------------------------------------------------------------------------------------------------"
"---------------------------------------------------------------------------------------------------------------------"
"---------------------------------------------------------------------------------------------------------------------"
"---------------------------------------------------------------------------------------------------------------------"

# User medical history

ID_medicalHistory = 'historial clínico'

cx = 'Cirugías'
hosp = 'Hospitalizaciones en los últimos 3 meses'
atb = 'Consumo de ATB en los últimos 3 meses'

# Questions to get user habits
dict_medicalHistory_questions = {cx: "¿Se ha sometido a cirugías? ({0}/{1}) ".format(yes,no),
                                 hosp: "¿Ha estado hospitalizado en los últimos 3 meses? ({0}/{1}) ".format(yes,no),
                                 atb: "¿Ha tenido consumo de ATB en los ultimos 3 meses ? ({0}/{1}) ".format(yes,no)
                                 }

"---------------------------------------------------------------------------------------------------------------------"
"---------------------------------------------------------------------------------------------------------------------"
"---------------------------------------------------------------------------------------------------------------------"
"---------------------------------------------------------------------------------------------------------------------"
"---------------------------------------------------------------------------------------------------------------------"
"---------------------------------------------------------------------------------------------------------------------"
"---------------------------------------------------------------------------------------------------------------------"
"---------------------------------------------------------------------------------------------------------------------"

dict_profile_questions = {ID_basicInfo: dict_info_questions,
                          ID_habits: dict_habits_questions,
                          ID_medicalHistory: dict_medicalHistory_questions
                          }
