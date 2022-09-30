import socket
import pickle
from ..Message import Message

'''
    Client class to communicate with TestServer
'''
class Client():
    def __init__(self) -> None:
        self.HOST = 'localhost'
        self.PORT = 8000
        self.socket = socket.socket()
    
    def send_message(self, message : Message):
        send_data = pickle.dumps(message)
        self.socket.sendall(send_data)

    def receive_message(self) -> Message:
        rec_data = self.socket.recv(1024)
        unpacked_data = pickle.loads(rec_data)
        return unpacked_data

    def __enter__(self):
        self.socket.connect((self.HOST, self.PORT))
        return self
    
    def __exit__(self, *args):
        self.socket.shutdown(socket.SHUT_RDWR)
        self.socket.close()


