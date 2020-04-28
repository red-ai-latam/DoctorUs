from View.DoctorUsView import DoctorUsView
from Model.DoctorUsModel import DoctorUsModel
from Config.basics import *
from Config.userProfileQuestions import dict_profile_questions
from Config.userMedicalProfileQuestions import dict_medicalProfile_questions


class DoctorUsController:
    """

    """

    def __init__(self, view: DoctorUsView, model: DoctorUsModel):
        self.view = view
        self.model = model

    def run(self):

        # Terms & Conditions
        if self.view.startChat() == yes:

            self.getProfileInfo()
            self.getMedicalProfileInfo()


        else:
            print("Gracias, adios :c")

    # Get info about user, habits, medical records
    def getProfileInfo(self):
        for id_dict in dict_profile_questions:
            self.model.updateCompleteInfo(id_dict, self.view.getProfileInfo(dict_profile_questions[id_dict], id_dict))

    def getMedicalProfileInfo(self):
        for id_dict in dict_medicalProfile_questions:
            self.model.updateCompleteInfo(id_dict,
                                          self.view.getMedicalProfileInfo(dict_medicalProfile_questions[id_dict],
                                                                          id_dict))

    # Just to debug
    def printModel(self):
        self.model.printModel()

