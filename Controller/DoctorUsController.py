from View.DoctorUsView import DoctorUsView
from Model.DoctorUsModel import DoctorUsModel
from Config.basics import *
from Config.Questions.userProfileQuestions import *
from Config.Questions.userMedicalProfileQuestions import *
from Config.Questions.userCovidQuestions import dict_covid_questions
from Config.Questions.userUrgencyQuestions import dict_urgency_questions
from Config.Questions.userSpecSymptoms import dict_specSymptoms_questions
from Config.Questions.userInSpecSymptoms import dict_inSpecSymptoms_questions
from Config.Scores.threshold import MIN_RISK_SCORE_RX, MIN_PROB_PRE_TEST, INSPECIFIC_SYMPTOMS_THRESHOLD


class DoctorUsController:
    """

    """

    def __init__(self, view: DoctorUsView, model: DoctorUsModel):
        self.view = view
        self.model = model

    def run(self):

        # Terms & Conditions
        if self.view.startChat():
            try:
                # Profile info and risk score from profile
                self.getProfileInfo()
                self.model.calculateRiskScore()

                # Exposition to COVID to get exposicion score
                self.askUser(ID_COVID, dict_covid_questions, BINARY)
                self.model.calculateExpositionScore()

                self.model.calculatePreTestScore()

                # Urgency info
                self.askUser(ID_URGENCY, dict_urgency_questions, FUZZY)
                self.model.calculateUrgencyState()

                # Check if is a urgency
                if self.model.checkUrgency():
                    self.view.alertUser(ID_URGENCY)
                else:
                    # Check if user has any symptoms
                    if self.view.hasSymptoms():
                        self.askUser(ID_SPEC_SYMP, dict_specSymptoms_questions, BINARY)
                        self.model.calculateSpecificSymptomsScore()

                        # If has some combination of specific symptoms
                        if self.model.checkSpecificSymptoms():
                            self.view.alertUser(ID_SPEC_SYMP)
                            # Besides, if has high risk score than MIN_RISK_SCORE_RX
                            if self.model.getRiskScore() >= MIN_RISK_SCORE_RX:
                                self.view.alertUser(ID_ALERT_RX)
                        else:
                            # Inspecific symptoms
                            self.askUser(ID_IN_SPEC_SYMP, dict_inSpecSymptoms_questions, BINARY)
                            self.model.calculateInSpecificSymptomsScore()
                            self.model.calculateTotalScore()

                            # Total Score
                            if self.model.total_score >= INSPECIFIC_SYMPTOMS_THRESHOLD:
                                self.view.alertUser(ID_IN_SPEC_SYMP)
                            elif MIN_PROB_PRE_TEST <= self.model.total_score <= INSPECIFIC_SYMPTOMS_THRESHOLD:
                                self.view.alertUser(ID_ALERT_TELEMEDICINE)
                            else:
                                self.view.alertUser(ID_ALERT_LOWPROB)
                    else:
                        # TODO: Tiene sentido seguir preguntando sintomas si ya dijo que no tiene?
                        if self.model.getPreTestScore() >= MIN_PROB_PRE_TEST:
                            self.view.alertUser(ID_ALERT_PRE_TEST)
                        else:
                            self.view.alertUser(ID_ALERT_LOWPROB)
                self.model.calculateTotalScore()
                # self.printModel()
            except:
                # TODO: Determinar error, interactuar con usuario
                print("Excepcion")
        else:
            print("Gracias, adios :c")

    def askUser(self, ID, dict, typeOfQuestions):
        if typeOfQuestions == BINARY:
            ans = self.view.getBinaryAnswers(ID, dict)
        elif typeOfQuestions == TEXT:
            ans = self.view.getTextAnswers(ID, dict)
        elif typeOfQuestions == FUZZY:
            ans = self.view.getFuzzyAnswers(ID, dict)
        else:
            ans = {}
        self.model.updateCompleteInfo(ID, ans)

    # Get info about user, habits, medical records, previous disease
    def getProfileInfo(self):
        self.askUser(ID_BASIC_INFO, dict_info_questions, TEXT)
        self.askUser(ID_HABITS, dict_habits_questions, BINARY)
        self.askUser(ID_MEDICAL_HISTORY, dict_medicalHistory_questions, BINARY)
        self.askUser(ID_PREVIOUS_DISEASE, dict_medicalProfile_questions, TEXT)

    # Just to debug
    def printModel(self):
        self.view.printModel(self.model)
