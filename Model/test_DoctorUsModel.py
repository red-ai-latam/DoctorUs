from unittest import TestCase

from Config.Questions.userProfileQuestions import *
from Config.Questions.userMedicalProfileQuestions import *
from Config.Questions.userCovidQuestions import *
from Config.Questions.userUrgencyQuestions import *
from Config.Questions.userSpecSymptoms import *
from Config.Questions.userInSpecSymptoms import *
from Model.DoctorUsModel import DoctorUsModel
from View.DoctorUsView import DoctorUsView
from Config.basics import *

# Aqui cambiar edad


dict_info_questions = {age: "27"}

# Aqui cambiar habitos
dict_habits_questions = {tbq: "n",
                         oh: "n",
                         ilegal_drugs: "n",
                         urine_state: "n",
                         defecate_state: "n"
                         }
# Aqui cambiar historial medico
dict_medicalHistory_questions = {cx: "n",
                                 hosp: "n",
                                 atb: "n"
                                 }

# Agregar ECNT, alergias y farmacos
list_ECNT = []
list_allergies = []
list_legalDrugs = []

# Aqui cambiar exposición
dict_covid_questions = {lockdown: "n",
                        travels: "n",
                        be_in_touch: "s"}

# Aqui cambiar datos de urgencia
dict_urgency_questions = {chest_pain: "n",
                          disnea: "0",
                          conscience: "n",
                          blue: "n"
                          }

# Aqui cambiar sintomas especificos
dict_specSymptoms_questions = {fever: "n",
                               cough: "n",
                               anosmia: "n"
                               }
# Aqui cambiar sintomas inespecificos
dict_inSpecSymptoms_questions = {mialgia: "n",
                                 cefalea: "n",
                                 escalofrios: "n",
                                 diarrea: "n",
                                 odinofagia: "n",
                                 skill_injury: "n"}

view = DoctorUsView()

model = DoctorUsModel()
model.userModel[ID_BASIC_INFO] = dict_info_questions
model.userModel[ID_HABITS] = dict_habits_questions
model.userModel[ID_MEDICAL_HISTORY] = dict_medicalHistory_questions
model.userModel[ID_ecnt] = list_ECNT
model.userModel[ID_allergies] = list_allergies
model.userModel[ID_legalDrugs] = list_legalDrugs
model.userModel[ID_COVID] = dict_covid_questions
model.userModel[ID_URGENCY] = dict_urgency_questions
model.userModel[ID_SPEC_SYMP] = dict_specSymptoms_questions
model.userModel[ID_IN_SPEC_SYMP] = dict_inSpecSymptoms_questions


class TestDoctorUsModel(TestCase):
    def test_calculate_score(self):
        self.fail()

    def test_calculate_exposition_score(self):
        dict_covid_questions = {lockdown: "s",
                                travels: "n",
                                be_in_touch: "n"}
        model.userModel[ID_COVID] = dict_covid_questions

        model.calculateExpositionScore()

        self.assertEqual(model.getExpositionScore(), 1)

    def test_calculate_risk_score(self):
        self.fail()

    def test_calculate_pre_test_score(self):
        self.fail()

    def test_calculate_specific_symptoms_score(self):
        self.fail()

    def test_calculate_in_specific_symptoms_score(self):
        self.fail()

    def test_calculate_total_score(self):
        self.fail()
