from Config.Scores.weights import *
from Config.Scores.threshold import *
from Config.Questions.userUrgencyQuestions import ID_urgency, disnea
from Config.Questions.userSpecSymptoms import *
from Config.Questions.userInSpecSymptoms import ID_inspec_symp


class DoctorUsModel:
    """


    """

    def __init__(self):
        self.userModel = {}
        self.userModel[ID_basicInfo] = {}
        self.userModel[ID_habits] = {}
        self.userModel[ID_medicalHistory] = {}
        self.userModel[ID_ecnt] = []
        self.userModel[ID_allergies] = []
        self.userModel[ID_legalDrugs] = []
        self.userModel[ID_covid] = {}
        self.userModel[ID_urgency] = {}
        self.userModel[ID_spec_symp] = {}
        self.userModel[ID_inspec_symp] = {}

        self.exposition_score = 0
        self.risk_score = 0
        self.pretest_score = 0
        self.specificSymptoms_score = 0
        self.inspecificSymptoms_score = 0

        self.total_score = 0

        self.urgency = False
        self.specificSymptoms = False

    # Update with a full dictionary of info
    def updateCompleteInfo(self, key, d):
        self.userModel[key] = d

    def calculateScore(self, ID, score, dict_weigths):
        for key, value in self.userModel[ID].items():
            if value == yes:
                score += dict_weigths[key]

    # Add each affirmative response according his weight
    def calculateExpositionScore(self):
        self.calculateScore(ID_covid, self.exposition_score, score_exposition)

    # Same as above. For ECNT, each one is added.
    # TODO: generar un vector de pesos para las distintas ENCT. Aca se considera el mismo peso para todas
    def calculateRiskScore(self):
        age_score = (score_risk[age] if int(self.userModel[ID_basicInfo][age]) >= MIN_AGE_RISK else 0)
        tbq_score = (score_risk[tbq] if self.userModel[ID_habits][tbq] == yes else 0)
        oh_score = (score_risk[oh] if self.userModel[ID_habits][oh] == yes else 0)
        ecnt_score = score_risk[ID_ecnt] * len(self.userModel[ID_ecnt])

        self.risk_score = age_score + tbq_score + oh_score + ecnt_score

    # TODO: Revisar, me hace sentido que sea así en vez de multiplicar, pues ambos casos son peligrosos por si solos
    def calculatePreTestScore(self):
        self.pretest_score = max(self.risk_score, self.exposition_score)

    def calculateSpecificSymptomsScore(self):
        self.calculateScore(ID_spec_symp, self.specificSymptoms_score, score_spec_sympt)

    def calculateInSpecificSymptomsScore(self):
        self.calculateScore(ID_inspec_symp, self.inspecificSymptoms_score, score_inspec_sympt)

    def calculateTotalScore(self):
        self.total_score = self.exposition_score + self.risk_score + self.specificSymptoms_score + self.inspecificSymptoms_score

    # If has any symptoms or disnea bigger than MIN_DISNEA_RISK_VALUE
    def checkUrgency(self):
        for key, value in self.userModel[ID_urgency].items():
            if key == disnea and int(self.userModel[ID_urgency][disnea]) >= MIN_DISNEA_RISK_VALUE:
                self.urgency = True
                return True
            elif self.userModel[ID_urgency][key] == yes:
                self.urgency = True
                return True
        self.urgency = False
        return False

    # If prob pre-test is high and any combination except cough-anosmia, then COVID risk
    # TODO: tos y anosmia no? Como agrego disnea?
    def checkSpecificSymptoms(self):
        dict_specSymptoms = self.userModel[ID_spec_symp]
        if self.pretest_score >= MIN_PROB_PRE_TEST:
            if dict_specSymptoms[fever] == yes:
                if dict_specSymptoms[cough] == yes or dict_specSymptoms[anosmia] == yes:
                    self.specificSymptoms = True
                    return True
        return False

    def getRiskScore(self):
        return self.risk_score

    def getPreTestScore(self):
        return self.pretest_score

    def getTotalScore(self):
        return self.total_score

    def printModel(self):
        for key in self.userModel:
            if isinstance(self.userModel[key], dict):
                for internKey in self.userModel[key]:
                    print("{0} , {1}".format(internKey, self.userModel[key][internKey]))
            else:
                print(self.userModel[key])
