# import infermedica_api
#
# infermedica_api.configure(app_id="f770ff52", app_key="ccedb8d1ebfbc89abd48aab8a5359185",
#                           model="infermedica-es-xl",
#                           api_version='covid19')
#
# api = infermedica_api.get_api()
#
# print(type(api).__name__)
#
#
# # risk_factor = api.risk_factors_list()
# # print(risk_factor)
#
#
#
# # Create diagnosis object with initial patient information.
# # Note that time argument is optional here as well as in the add_symptom function
# request = infermedica_api.Diagnosis(sex='male', age=35)
#
# request.add_symptom('s_21', 'present')
# request.add_symptom('s_98', 'present')
# request.add_symptom('s_107', 'absent')
#
# # call diagnosis
# api.diagnosis(request)
#
# # Access question asked by API
# print(request.question)
# print(request.question.text)  # actual text of the question
# print(request.question.items)  # list of related evidences with possible answers
# print(request.question.items[0]['id'])
# print(request.question.items[0]['name'])
# print(request.question.items[0]['choices'])  # list of possible answers
# print(request.question.items[0]['choices'][0]['id'])  # answer id
# print(request.question.items[0]['choices'][0]['label'])  # answer label
#
#
# # Next update the request and get next question:
# # Just example, the id and answer shall be taken from the real user answer
# request.add_symptom(request.question.items[0]['id'], request.question.items[0]['choices'][1]['id'])
# request.add_symptom(request.question.items[0]['id'], request.question.items[0]['choices'][1]['id'])
# request.add_symptom(request.question.items[0]['id'], request.question.items[0]['choices'][1]['id'])
#
# # call diagnosis method again
# request = api.diagnosis(request)
#
# print(request.question.text)



# ... and so on, until you decide to stop the diagnostic interview.


from InterviewFlow.CovidFlow import CovidFlow

engine = CovidFlow()

request = {
    "text" : "hola",
    "user_name" : "david"
}
response = engine.handle_message(request)

for r in response:
    print(r)

request = {
    "text" : "hola",
    "user_name" : "david",
    "age" : "jj",
    "sex" : "hombre"
}

response = engine.handle_message(request)
for r in response:
    print(r)

request = {
    "text" : "hola",
    "user_name" : "david",
    "age" : "78",
    "sex" : "hombre"
}

response = engine.handle_message(request)
for r in response:
    print(r)


request = {
    "text" : "hola",
    "user_name" : "david",
    "age" : "78",
    "sex" : "hombre",
    "evidence" : [
        {"id": "p_18", "choice_id": "absent"},
        {"id": "p_19", "choice_id": "present"},
        {"id": "p_24", "choice_id": "present"},
        {"id": "p_22", "choice_id": "present"},
    ]
}

response = engine.handle_message(request)
for r in response:
    print(r)

