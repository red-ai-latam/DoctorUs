from Config.userProfileQuestions import ID_basicInfo, ID_habits, ID_medicalHistory
from Config.userMedicalProfileQuestions import ID_ecnt, ID_allergies, ID_legalDrugs

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

    # Update with a full dictionary of info
    def updateCompleteInfo(self, key, d):
        self.userModel[key] = d

    def printModel(self):
        for key in self.userModel:
            if isinstance(self.userModel[key], dict):
                for internKey in self.userModel[key]:
                    print("{0} , {1}".format(internKey, self.userModel[key][internKey]))
            else:
                print(self.userModel[key])



