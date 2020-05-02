from Config.Scores.weights import *
from Config.Scores.threshold import *
from Config.basics import *
from Config.Questions.userSpecSymptoms import *

class DoctorUsModel:
    """


    """

    def __init__(self):
        self.userModel = {ID_BASIC_INFO: {}, ID_HABITS: {}, ID_MEDICAL_HISTORY: {}, ID_PREVIOUS_DISEASE: {},
                          ID_COVID: {}, ID_URGENCY: {}, ID_SPEC_SYMP: {}, ID_IN_SPEC_SYMP: {}}

        self.exposition_score = 0
        self.risk_score = 0
        self.pretest_score = 0
        self.specificSymptoms_score = 0
        self.inspecificSymptoms_score = 0

        self.total_score = 0

        self.urgency = False
        self.specificSymptoms = False

    # Update with a full dictionary of info
    # For PREVIOUS DISEASE, each value of dict should be convert in a list
    # because every ECNT, allergies or drugs are input together
    # d[k] = " disease1,disease2"
    def updateCompleteInfo(self, key, d):
        if key == ID_PREVIOUS_DISEASE:
            for k in d:
                self.userModel[key][k] = d[k].split(',') if len(d[k]) > 1 else [d[k]]
            print(self.userModel[ID_PREVIOUS_DISEASE])
        else:
            self.userModel[key] = d

    def calculateScore(self, ID, dict_weigths):
        score_cache = 0
        for key, value in self.userModel[ID].items():
            if value == YES:
                score_cache += dict_weigths[key]
        return score_cache

    # Add each affirmative response according his weight
    def calculateExpositionScore(self):
        self.exposition_score = self.calculateScore(ID_COVID, dict_weights_exposition)


    # Same as above. For ECNT, each one is added.
    # TODO: generar un vector de pesos para las distintas ENCT. Aca se considera el mismo peso para todas
    def calculateRiskScore(self):
        try:
            age_score = (dict_weight_risk[age] if int(self.userModel[ID_BASIC_INFO][age]) >= MIN_AGE_RISK else 0)
            tbq_score = (dict_weight_risk[tbq] if self.userModel[ID_HABITS][tbq] == YES else 0)
            oh_score = (dict_weight_risk[oh] if self.userModel[ID_HABITS][oh] == YES else 0)
            ecnt_score = dict_weight_risk[ID_ecnt] * len(self.userModel[ID_PREVIOUS_DISEASE][ID_ecnt])
            self.risk_score = age_score + tbq_score + oh_score + ecnt_score
        except ValueError:
            self.risk_score = 0

    # TODO: Revisar, me hace sentido que sea así en vez de multiplicar, pues ambos casos son peligrosos por si solos
    def calculatePreTestScore(self):
        self.pretest_score = max(self.risk_score, self.exposition_score)

    def calculateUrgencyState(self):
        for key, value in self.userModel[ID_URGENCY].items():
            if int(self.userModel[ID_URGENCY][key]) >= MIN_URGENCY_VALUE:
                self.urgency = True
                return
        self.urgency = False

    def calculateSpecificSymptomsScore(self):
        self.specificSymptoms_score = self.calculateScore(ID_SPEC_SYMP, dict_weight_specSympt)


    def calculateInSpecificSymptomsScore(self):
        self.inspecificSymptoms_score = self.calculateScore(ID_IN_SPEC_SYMP, dict_weight_inSpecSymp)

    def calculateTotalScore(self):
        self.total_score = self.exposition_score + self.risk_score + self.specificSymptoms_score + self.inspecificSymptoms_score

    def checkUrgency(self):
        return self.urgency

    # If prob pre-test is high and any combination except cough-anosmia, then COVID risk
    # TODO: tos y anosmia no? Como agrego disnea?
    def checkSpecificSymptoms(self):
        dict_specSymptoms = self.userModel[ID_SPEC_SYMP]
        if self.pretest_score >= MIN_PROB_PRE_TEST:
            if dict_specSymptoms[fever] == YES:
                if dict_specSymptoms[cough] == YES or dict_specSymptoms[anosmia] == YES:
                    self.specificSymptoms = True
                    return True
        return False

    def getRiskScore(self):
        return self.risk_score

    def getExpositionScore(self):
        return self.exposition_score

    def getPreTestScore(self):
        return self.pretest_score

    def getSpecSymp(self):
        return self.specificSymptoms_score

    def getInSpecSymp(self):
        return self.inspecificSymptoms_score

    def getTotalScore(self):
        return self.total_score

    def printModel(self):
        for key in self.userModel:
            if isinstance(self.userModel[key], dict):
                for internKey in self.userModel[key]:
                    print("{0} , {1}".format(internKey, self.userModel[key][internKey]))
            else:
                print("{0} : {1}".format(key,self.userModel[key]))
