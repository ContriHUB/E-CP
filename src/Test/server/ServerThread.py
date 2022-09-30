from threading import Thread

'''
    Thread class to run TestServer on
'''
class ServerThread(Thread):
    def __init__(self, server):
        super().__init__()
        self.server = server

    def run(self) -> None:
        self.server.start_test_server()