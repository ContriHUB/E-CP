'''
    Problem class
'''

class Problem:
    def __init__(self, name, tests = []) -> None:
        self.name = name
        self.tests = tests