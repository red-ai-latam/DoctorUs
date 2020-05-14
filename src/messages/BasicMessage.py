import enum

class Types(enum.Enum):
    INFO = "info"
    QUESTION = "question"
    ANSWER = "answer"





class BasicMessage:
    """
    Message to have a internal representation of request send by user
    Add any atribute needed to integrate with a UI

    """


    def __init__(self):
        self._id = None
        self._type = None
        self._payload = {
            ""
        }


    def add_hello_msg(self, user_name : str, text :str):
        self._payload["user_name"] = user_name
        self._payload["text"] = text

    def get_text(self):
        if "text" in self._payload:
            return self._payload["text"]
        else:
            return ""



