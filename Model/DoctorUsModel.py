from View.start_conversation_text import age, sex
from Utils.constants import SEX_NORM, USER_PROFILE, USER_EVIDENCE, USER_DIAGNOSES, USER_TRIAGE
from Utils import apiaccess

# Query for all observation names and store them
naming = apiaccess.get_observation_names(apiaccess.auth_string, apiaccess.case_id, apiaccess.language_model)


class DoctorUsModel:
    """


    """

    def __init__(self):
        self.userModel = {
            USER_PROFILE: {},
            USER_EVIDENCE: [],
            USER_DIAGNOSES: [],
            USER_TRIAGE: {}

        }

    # Update with a full dictionary of info
    def update_user_profile(self, values):
        self.userModel[USER_PROFILE] = values

    def get_age_and_sex(self):
        return int(self.userModel[USER_PROFILE][age]), SEX_NORM[self.userModel[USER_PROFILE][sex]]

    def summarise_evidence(self, evidence):
        apiaccess.name_evidence(evidence=evidence, naming=naming)
        self.userModel[USER_EVIDENCE] = evidence

    # Smell code, but maybe in future
    # we can pre-process data in different ways

    def summarise_diagnoses(self, diagnoses):
        self.userModel[USER_DIAGNOSES] = diagnoses

    def summarise_triage(self, triage):
        self.userModel[USER_TRIAGE] = triage

    def get_evidence(self):
        return self.userModel[USER_EVIDENCE]

    def get_diagnoses(self):
        return self.userModel[USER_DIAGNOSES]

    def get_triage(self):
        return self.userModel[USER_TRIAGE]
