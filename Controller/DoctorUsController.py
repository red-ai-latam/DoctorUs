from View.DoctorUsView import DoctorUsView
from Model.DoctorUsModel import DoctorUsModel
from Config.basics import *
from Config.Questions.userProfileQuestions import dict_profile_questions
from Config.Questions.userMedicalProfileQuestions import dict_medicalProfile_questions
from Config.Questions.userCovidQuestions import dict_covid_questions, ID_covid
from Config.Questions.userUrgencyQuestions import dict_urgency_questions, ID_urgency
from Config.Questions.userSpecSymptoms import dict_specSymptoms_questions, ID_spec_symp
from Config.Questions.userInSpecSymptoms import dict_inSpecSymptoms_questions, ID_inspec_symp
from Config.Scores.threshold import MIN_RISK_SCORE_RX, MIN_PROB_PRE_TEST, INSPECIFIC_SYMPTOMS_THRESHOLD


class DoctorUsController:
    """

    """

    def __init__(self, view: DoctorUsView, model: DoctorUsModel):
        self.view = view
        self.model = model

    def run(self):

        # Terms & Conditions
        if self.view.startChat() == yes:

            # Profile info and risk score from profile
            self.getProfileInfo()
            self.getMedicalProfileInfo()
            self.model.calculateRiskScore()

            # Exposition to COVID to get exposicion score
            self.getInfo(ID_covid, dict_covid_questions)
            self.model.calculateExpositionScore()

            self.model.calculatePreTestScore()

            # Urgency info
            self.getInfo(ID_urgency, dict_urgency_questions)

            # Check if is a urgency
            if self.model.checkUrgency():
                self.view.alertEmergency()
            else:
                # Check if user has any symptoms
                if self.view.hasSymptoms():
                    self.getInfo(ID_spec_symp, dict_specSymptoms_questions)

                    # If has some combination of specific symptoms
                    if self.model.checkSpecificSymptoms():
                        self.view.alertSpecificSymptoms()
                        # Besides, if has high risk score than MIN_RISK_SCORE_RX
                        if self.model.getRiskScore() >= MIN_RISK_SCORE_RX:
                            self.view.alertRx()
                    else:
                        # Inspecific symptoms
                        self.getInfo(ID_inspec_symp, dict_inSpecSymptoms_questions)

                        # Total Score
                        if self.model.total_score >= INSPECIFIC_SYMPTOMS_THRESHOLD:
                            self.view.alertInspecificSymptoms()
                        elif self.model.total_score >= MIN_PROB_PRE_TEST and self.model.total_score <= INSPECIFIC_SYMPTOMS_THRESHOLD:
                            self.view.alertTelemedicine()
                        else:
                            self.view.alertLowProb()


                else:
                    # TODO: Tiene sentido seguir preguntando sintomas si ya dijo que no tiene?
                    if self.model.getPreTestScore() >= MIN_PROB_PRE_TEST:
                        self.view.alertPreTest()
                    else:
                        self.view.alertLowProb()

        else:
            print("Gracias, adios :c")

    # Get info about user, habits, medical records
    def getProfileInfo(self):
        for id_dict in dict_profile_questions:
            self.getInfo(id_dict, dict_profile_questions[id_dict])

    def getMedicalProfileInfo(self):
        for id_dict in dict_medicalProfile_questions:
            self.model.updateCompleteInfo(id_dict,
                                          self.view.getMedicalProfileInfo(dict_medicalProfile_questions[id_dict],
                                                                          id_dict))

    def getInfo(self, ID, dict):
        self.model.updateCompleteInfo(ID, self.view.getInfo(dict, ID))

    # Just to debug
    def printModel(self):
        self.model.printModel()
