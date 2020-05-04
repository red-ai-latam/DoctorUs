from View.DoctorUsView import DoctorUsView
from Model.DoctorUsModel import DoctorUsModel


class DoctorUsController:
    """

    """

    def __init__(self):
        self.view = DoctorUsView(self)
        self.model = DoctorUsModel()

    def run(self):
        # Terms & Conditions
        if self.view.init_program and self.view.accept_legal_info():
            try:
                # Profile info and risk score from profile
                self.view.ask_user_profile()

                # Chatbot
                self.view.chatbox(self.model.get_age_and_sex()[0], self.model.get_age_and_sex()[1])

                # Summarise
                self.view.show_summary(evidence=self.model.get_evidence(), triage=self.model.get_triage(),
                                       diagnoses=self.model.get_diagnoses())

            except NotImplementedError:
                print("EXIT PROGRAM")

            except Exception as err:
                # TODO: Determinar error, interactuar con usuario
                print(err.__cause__)
        else:
            print("Gracias, adios :c")

    def save_user_profile(self, values):
        self.model.update_user_profile(values)

    # Save in model
    def save_user_diagnosis(self, evidence, diagnoses, triage):
        self.model.summarise_evidence(evidence)
        self.model.summarise_diagnoses(diagnoses)
        self.model.summarise_triage(triage)
