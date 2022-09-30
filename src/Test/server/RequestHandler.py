from threading import Thread
import pickle
from socketserver import BaseRequestHandler
from ..TestTimer import TestTimer
from ..Message import Message

MAX_LIMIT = 1024

'''
    Class to hanlde requests sent to server
'''
class RequestHandler(BaseRequestHandler):
    def __handle_end_test(self):
        # Stop server thread from another thread to prevent deadlock
        th = Thread(target = self.server.stop_test_server)
        th.start()

        send_data = Message('Test ended...')
        packed_data = pickle.dumps(send_data)
        self.request.sendall(packed_data)

    def __handle_get_rem_time(self):
        test_timer : TestTimer = self.server.test_timer
        rem_time = test_timer.get_rem_time()

        send_data = Message(rem_time)
        packed_data = pickle.dumps(send_data)
        self.request.sendall(packed_data)

    def __handle_invalid_request(self):
        send_data = Message('Invalid request')
        packed_data = pickle.dumps(send_data)
        self.request.sendall(packed_data)


    def handle(self) -> None:
        rec_data = self.request.recv(MAX_LIMIT)
        unpacked_data = pickle.loads(rec_data)

        if unpacked_data.message == 'STOP':
            self.__handle_end_test()
        elif unpacked_data.message == 'GET-REM-TIME':
            self.__handle_get_rem_time()
        else:
            self.__handle_invalid_request()

