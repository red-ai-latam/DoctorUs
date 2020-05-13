class ILogData:

    def __init__(self, tag, _type, message, description=None, date=None):
        self.tag = tag
        self.type = _type
        self.message = message
        self.description = description
        self.date = date