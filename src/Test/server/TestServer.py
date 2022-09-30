from socketserver import TCPServer
from ..TestTimer import TestTimer

'''
    Server which manages current test, and respond to requests from Client
'''

class TestServer(TCPServer):
    def __init__(self, server_address: tuple[str, int], RequestHandlerClass, timer_function, interval = 20) -> None:
        super().__init__(server_address, RequestHandlerClass)

        self.test_timer = TestTimer(interval, timer_function, args=[self])
        self.test_timer.start()

    def start_test_server(self):
        print('Starting test server...')
        super().serve_forever()

    def stop_test_server(self):
        self.test_timer.cancel()
        print('Stopping test server...')
        super().shutdown()