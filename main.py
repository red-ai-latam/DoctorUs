from Controller import DoctorUsController


def run():
    # credentials.get_credentials()

    # Query for all observation names and store them. In a real chatbot, this
    # could be done once at initialisation and used for handling all events by
    # one worker. This is an id2name mapping.
    # naming = apiaccess.get_observation_names(auth_string, case_id, args.model)

    # Init program
    controller = DoctorUsController.DoctorUsController()

    controller.run()

    # Read patient's complaints by using /parse endpoint.
    # mentions = conversation.read_complaints(auth_string, case_id, args.model)

    # Keep asking diagnostic questions until stop condition is met (all of this
    # by calling /diagnosis endpoint) and get the diagnostic ranking and triage
    # (the latter from /triage endpoint).
    # evidence = apiaccess.mentions_to_evidence(mentions)
    # evidence, diagnoses, triage = conversation.conduct_interview(evidence, age,sex, case_id,auth_string,args.model)

    # Add `name` field to each piece of evidence to get a human-readable
    # summary.
    # apiaccess.name_evidence(evidence, naming)

    # Print out all that we've learnt about the case and finish.
    # print()
    # conversation.summarise_all_evidence(evidence)
    # conversation.summarise_diagnoses(diagnoses)
    # conversation.summarise_triage(triage)


if __name__ == "__main__":
    run()
