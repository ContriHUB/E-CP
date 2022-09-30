'''
    messages are exchanged between client and server with the help of Message objects
'''

class Message:
    def __init__(self, message) -> None:
        self.message = message
