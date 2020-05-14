import infermedica_api
from infermedica_api.exceptions import MissingConfiguration
import logging

# TODO: Cada vez que haya un cambio en el modelo, deberia guardarse en una BD para respaldo
class BasicUserModel:
    def __init__(self, api_model, api_version):
        # TODO: Agregar como atributo toda la info que se quiera recoger

        # Represent user data
        self.actual_diagnosis = infermedica_api.Diagnosis

        # Infermedica API configuration
        infermedica_api.configure(app_id="***", app_key="***",
                                  model=api_model,
                                  api_version=api_version)

        try:
            self.infermedica_api = infermedica_api.get_api()
        except MissingConfiguration as e:
            logging.getLogger("transitions").error(msg='Error in module {0} : {1}'.format(type(self).__name__, str(e)))
            raise Exception

    # Setter to age and sex
    def set_sex_and_age(self, sex, age):
        self.actual_diagnosis = self.actual_diagnosis(sex=sex, age=age)

    def call_diagnosis(self):
        try:
            return self.infermedica_api.diagnosis(self.actual_diagnosis)
        except Exception as e:
            logging.getLogger("transitions").error(msg='Error in module %s' % type(self).__name__, stack_info=True)

    def call_triage(self):
        try:
            return self.infermedica_api.triage(self.actual_diagnosis)
        except Exception as e:
            logging.getLogger("transitions").error(msg='Error in module %s' % type(self).__name__, stack_info=True)

    def get_evidence_questions(self):
        return self.actual_diagnosis.question

    def should_stop(self):
        return self.actual_diagnosis.should_stop

    def add_evidence(self, id, choice):
        self.actual_diagnosis.add_evidence(_id=id, state=choice)

    def reset_model(self):
        self.actual_diagnosis = infermedica_api.Diagnosis
