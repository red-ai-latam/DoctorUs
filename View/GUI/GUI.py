import PySimpleGUI as sg
from .chatText import *
from Config.basics import *

OK = 'OK'
CANCEL = 'Cancel'
SUBMIT = 'Submit'
YES_VIEW = 'Yes'
NO_VIEW = 'No'
dict_events = {OK: True,
               YES_VIEW: True,
               SUBMIT: True,
               NO_VIEW: False,
               CANCEL: False
               }

dict_size_window = {
    ID_BASIC_INFO: {
        'Text': (25, 1), "Input Text": (30, 1)
    },
    ID_PREVIOUS_DISEASE: {
        'Text': (15, 4), "Input Text": (25, 4)
    },
    ID_COVID: {
        'Text': (30, 2)
    },
    ID_HABITS: {
        'Text': (25, 1)
    },
    ID_MEDICAL_HISTORY: {
        'Text': (25, 2)
    },
    ID_URGENCY: {
        'Text': (30, 2)
    },
    ID_SPEC_SYMP: {
        'Text': (25,1)
    },
    ID_IN_SPEC_SYMP: {
        'Text': (25,1)
    }

}


def helloWorld():
    return dict_events[sg.popup_ok_cancel(START_TEXT, title='Doctor US')]


def legalInfo():
    return dict_events[sg.popup_scrolled(LEGAL_INFO, yes_no=True, title=TITLE)]


def inputTextWindow(ID_window, dict_questions):
    layout = []
    for k, v in dict_questions.items():
        format_ = [sg.Text(v, size=dict_size_window[ID_window]['Text']),
                   sg.InputText(key=k, size=dict_size_window[ID_window]['Input Text'])]
        layout.append(format_)
    layout.append([sg.Submit(), sg.Cancel()])

    window = sg.Window(ID_window, layout)
    event, values = window.read()
    window.close()

    return dict_events[event], values


def yesNoWindow(ID_window, dict_questions):
    layout = []
    for k, v in dict_questions.items():
        format_ = [sg.Text(v, size=dict_size_window[ID_window]['Text']),
                   sg.InputCombo((YES, NO), size=(5, 1), key=k, default_value=NO)]
        layout.append(format_)
    layout.append([sg.Submit(), sg.Cancel()])

    window = sg.Window(ID_window, layout)
    event, values = window.read()
    window.close()

    return dict_events[event], values


def slideBarWindow(ID_window, dict_questions):
    layout = []
    for k, v in dict_questions.items():
        format_ = [sg.Text(v, size=dict_size_window[ID_window]['Text']),
                   sg.Slider(range=(0, 5), orientation='h', size=(10, 20), default_value=0)]
        layout.append(format_)
    layout.append([sg.Submit(), sg.Cancel()])

    window = sg.Window(ID_window, layout)
    event, values = window.read()
    window.close()

    return dict_events[event], values


def generalYesNoWindows(text):
    return dict_events[sg.popup_yes_no(text, title='Doctor US')]


def generalDisplayWindos(text):
    return sg.popup_ok(text, title="Resultado")
