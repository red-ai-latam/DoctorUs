from unittest import TestCase


class TestCovidFlow(TestCase):
    def test_handle_message(self):
        from src.interviews.CovidFlow import CovidFlow, INIT, CREATE, DIAGNOSIS, TRIAGE

        engine = CovidFlow()

        self.assertEqual(engine.state, INIT)

        request = {
            "text": "hola",
            "user_name": "david"
        }
        response = engine.handle_message(request)
        for r in response:
            print(r)

        self.assertEqual(engine.state, CREATE)

        request = {
            "text": "hola",
            "user_name": "david",
            "age": "jj",
            "sex": "hombre"
        }

        response = engine.handle_message(request)
        for r in response:
            print(r)

        self.assertEqual(engine.state, CREATE)

        request = {
            "text": "hola",
            "user_name": "david",
            "age": "78",
            "sex": "hombre"
        }

        response = engine.handle_message(request)
        for r in response:
            print(r)

        self.assertEqual(engine.state, DIAGNOSIS)
        self.assertEqual(response[len(response) - 2], "Empieza la entrevista !")

        request = {
            "text": "hola",
            "user_name": "david",
            "age": "78",
            "sex": "hombre",
            "evidence": [
                {"id": "p_18", "choice_id": "absent"},
                {"id": "p_19", "choice_id": "present"},
                {"id": "p_24", "choice_id": "present"},
                {"id": "p_22", "choice_id": "present"},
            ]
        }

        response = engine.handle_message(request)
        for r in response:
            print(r)

        self.assertEqual(engine.state, DIAGNOSIS)
        self.assertFalse(engine.user_model.should_stop())

        request = {
            "text": "hola",
            "user_name": "david",
            "age": "78",
            "sex": "hombre",
            "evidence": [
                {"id": "p_18", "choice_id": "absent"},
                {"id": "p_19", "choice_id": "present"},
                {"id": "p_24", "choice_id": "present"},
                {"id": "p_22", "choice_id": "present"},
                {"id": "p_23", "choice_id": "present"},
                {"id": "p_20", "choice_id": "present"},
            ]
        }

        engine.user_model.actual_diagnosis.should_stop = True

        response = engine.handle_message(request)
        for r in response:
            print(r)

        self.assertEqual(engine.state, TRIAGE)
        self.assertTrue(engine.user_model.should_stop())


        request = {
            "text": "chao",
            "user_name": "david",
            "age": "78",
            "sex": "hombre",
            "evidence": [
                {"id": "p_18", "choice_id": "absent"},
                {"id": "p_19", "choice_id": "present"},
                {"id": "p_24", "choice_id": "present"},
                {"id": "p_22", "choice_id": "present"},
                {"id": "p_23", "choice_id": "present"},
                {"id": "p_20", "choice_id": "present"},
            ]
        }

        response = engine.handle_message(request)
        for r in response:
            print(r)

        self.assertEqual(engine.state, INIT)

        for name,instance in engine.states.items():
            self.assertFalse(instance.check_new_state())
