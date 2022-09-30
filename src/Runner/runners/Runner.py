from abc import ABC, abstractmethod

'''
    Abstract base class for all runners
'''
class Runner(ABC):
    def __init__(self, dest, code_file) -> None:
        self.dest = dest
        self.code_file = code_file

    @abstractmethod
    def run_on_test_files(self):
        pass

    @abstractmethod
    def run_on_custom(self):
        pass