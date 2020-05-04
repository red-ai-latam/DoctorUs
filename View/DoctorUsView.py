from . import start_conversation_text
import PySimpleGUI as sg
from Utils import conversation


class DoctorUsView:
    """

    """

    def __init__(self, controller):
        self.init_program = self.hello_world()
        self.controller = controller

    def hello_world(self):
        event = sg.popup_ok_cancel(start_conversation_text.START_TEXT, title='Doctor US')
        if event == 'Cancel':  # quit if exit button
            return False
        elif event == 'OK':
            return True

    # Ask for legal conditions
    def accept_legal_info(self):
        event = sg.popup_scrolled(start_conversation_text.LEGAL_INFO, yes_no=True, title=start_conversation_text.TITLE)
        if event == 'No':  # quit if exit button
            return False
        elif event == 'Yes':
            return True

    # Ask questions in dict_questions. Return answers as a dict of text
    def ask_user_profile(self):
        layout = []
        for k, v in start_conversation_text.dict_info_questions.items():
            format_ = [sg.Text(v, size=(25, 1)),
                       sg.InputText(key=k, size=(30, 1))]
            layout.append(format_)
        layout.append([sg.Button('ENVIAR', bind_return_key=True),
                       sg.Button('SALIR')])

        window = sg.Window(title='Antecedentes', layout=layout)
        event, values = window.read()
        if event == 'SALIR':  # quit if exit button
            window.close()
            raise Exception
        elif event == 'ENVIAR':
            window.close()
            self.controller.save_user_profile(values)

    # TODO : hacerlo bonito. Ver como evitar que bloquee la terminal al usar Output, probar logging
    def chatbox(self, age, sex):
        sg.theme('Dark Blue 3')
        layout = [[sg.Text('DoctorUs dice', size=(20, 1))],
                  [sg.Output(size=(70, 20), font=('Helvetica 12'), key='-OUTPUT', )],
                  [sg.Multiline("Presiona PARTIR para empezar", size=(20, 2), font=('Helvetica 10'), key='-IN-',
                                do_not_clear=False, enter_submits=True),
                   sg.Button('PARTIR', bind_return_key=True),
                   sg.Button('LIMPIAR'),
                   sg.Button('SALIR')]]

        window = sg.Window('DoctorUs Chatbot', layout, font=('Helvetica', ' 13'), default_button_element_size=(8, 2))

        event, value = window.read()
        if event == 'SALIR':
            raise NotImplementedError("EXIT PROGRAM")
        elif event == 'LIMPIAR':
            window['-OUTPUT-'].update('')
        elif event == 'PARTIR':
            window['-IN-'].update('')
            try:
                evidence, diagnoses, triage = conversation.conduct_interview_gui(evidence=[], age=age, sex=sex,
                                                                                 windows=window)
                self.controller.save_user_diagnosis(evidence, diagnoses, triage)

            except NotImplementedError:
                raise NotImplementedError("EXIT PROGRAM")
            except Exception as err:
                raise err
            finally:
                window.close()

    #TODO: Doesnt Working
    def show_summary(self, evidence, diagnoses, triage):
        # List of evidences
        layout_evidence = []
        if evidence:
            for i, ev in enumerate(evidence):
                layout_evidence += [sg.Text(f'{i + 1}. '), sg.Text(ev)],

        # Triage results
        layout_diagnoses = []
        if diagnoses:
            for i, diag in enumerate(diagnoses):
                layout_diagnoses += [sg.Text(f'{i + 1}. '), sg.Text(diag["name"]), sg.Text(diag["probability"])],

        layout_triage = []
        if triage:
            layout_triage = [
                [sg.Text("Resumen")], [sg.Text(triage['description'])],
                [sg.Text("Recomendacion ")], [sg.Text(triage['label'])],
            ]

        layout_diagnoses.append(layout_triage)

        # Tabs
        layout = [[sg.TabGroup([[sg.Tab('Triage', layout_diagnoses), sg.Tab('Evidencia', layout_evidence)]])],
                  [[sg.Button('GUARDAR'), sg.Button('SALIR')]]]

        window = sg.Window('Resultados', layout, font=('Helvetica', ' 13'), default_button_element_size=(8, 2))

        event, value = window.read()
        if event == 'SALIR':
            window.close()
        elif event == 'GUARDAR':
            window.close()
