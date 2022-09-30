from threading import Timer
from datetime import datetime

'''
    TestTimer class to keep track of Test time
'''

class TestTimer(Timer):
    def __init__(self, interval: float, function, args = None, kwargs = None) -> None:
        super().__init__(interval, function, args, kwargs)
        self.start_time = datetime.now()

    def __get_elapsed_time(self):
        delta = datetime.now() - self.start_time
        return delta.seconds

    def get_rem_time(self):
        time_elapsed = self.__get_elapsed_time()
        return self.interval - time_elapsed

    def cancel(self) -> None:
        print('Cancelling test timer...')
        return super().cancel()