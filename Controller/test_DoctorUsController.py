from unittest import TestCase

from Config.Questions.userProfileQuestions import *
from Config.Scores.threshold import MIN_RISK_SCORE_RX, INSPECIFIC_SYMPTOMS_THRESHOLD, MIN_PROB_PRE_TEST
from Config.Questions.userMedicalProfileQuestions import *
from Config.Questions.userCovidQuestions import *
from Config.Questions.userUrgencyQuestions import *
from Config.Questions.userSpecSymptoms import *
from Config.Questions.userInSpecSymptoms import *
from Model.DoctorUsModel import DoctorUsModel
from View.DoctorUsView import DoctorUsView

# Aqui cambiar edad


dict_info_questions = {age: "80"}

# Aqui cambiar habitos
dict_habits_questions = {tbq: "s",
                         oh: "s",
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
list_ECNT = ['asd', 'asd', 'asd']
list_allergies = ['asd']
list_legalDrugs = ['asd']



# Aqui cambiar exposición
dict_covid_questions = {lockdown : "n",
                        travels : "n",
                        be_in_touch : "n"}


# Aqui cambiar datos de urgencia
dict_urgency_questions = {chest_pain: "n",
                          disnea: "1",
                          conscience: "n",
                          blue: "n"
                          }

# Aqui cambiar sintomas especificos
dict_specSymptoms_questions = {fever: "n",
                               cough: "n",
                               anosmia: "s"
                               }
# Aqui cambiar sintomas inespecificos
dict_inSpecSymptoms_questions = {mialgia : "s",
                                 cefalea : "n",
                                 escalofrios : "s",
                                 diarrea : "n",
                                 odinofagia : "s",
                                 skill_injury : "n"}


view = DoctorUsView()

model = DoctorUsModel()
model.userModel[ID_basicInfo] = dict_info_questions
model.userModel[ID_habits] = dict_habits_questions
model.userModel[ID_medicalHistory] = dict_medicalHistory_questions
model.userModel[ID_ecnt] = list_ECNT
model.userModel[ID_allergies] = list_allergies
model.userModel[ID_legalDrugs] = list_legalDrugs
model.userModel[ID_covid] = dict_covid_questions
model.userModel[ID_urgency] = dict_urgency_questions
model.userModel[ID_spec_symp] = dict_specSymptoms_questions
model.userModel[ID_inspec_symp] = dict_inSpecSymptoms_questions

class TestDoctorUsController(TestCase):
    def test_urgency(self):

        # Aqui cambiar datos de urgencia
        dict_urgency_questions = {chest_pain: "n",
                                  disnea: "5",
                                  conscience: "n",
                                  blue: "n"
                                  }
        model.userModel[ID_urgency] = dict_urgency_questions

        self.assertEqual(model.checkUrgency(), True)



    def test_complete(self):

        # Set


        # Profile info and risk score from profile
        model.calculateRiskScore()
        # self.assertEqual(model.getRiskScore(), 0)
        model.calculateExpositionScore()
        # self.assertEqual(model.getExpositionScore(), 0)
        model.calculatePreTestScore()
        self.assertEqual(model.getPreTestScore(), 10)


        if model.checkUrgency():
            view.alertEmergency()
            self.assertEqual(model.checkUrgency(), True)

        else:
            # Check if user has any symptoms
            if True:
                # If has some combination of specific symptoms
                if model.checkSpecificSymptoms():
                    view.alertSpecificSymptoms()
                    # Besides, if has high risk score than MIN_RISK_SCORE_RX
                    if model.getRiskScore() >= MIN_RISK_SCORE_RX:
                        view.alertRx()
                        self.assertGreaterEqual(model.getRiskScore() , MIN_RISK_SCORE_RX)
                else:
                    # Total Score
                    self.assertGreaterEqual(model.total_score, INSPECIFIC_SYMPTOMS_THRESHOLD)
                    if model.total_score >= INSPECIFIC_SYMPTOMS_THRESHOLD:

                        view.alertInspecificSymptoms()
                    elif model.total_score >= MIN_PROB_PRE_TEST and model.total_score <= INSPECIFIC_SYMPTOMS_THRESHOLD:
                        self.assertGreaterEqual(model.total_score, MIN_PROB_PRE_TEST)
                        self.assertLessEqual(model.total_score, INSPECIFIC_SYMPTOMS_THRESHOLD)
                        view.alertTelemedicine()
                    else:
                        self.assertLess(model.total_score, MIN_PROB_PRE_TEST)
                        view.alertLowProb()


