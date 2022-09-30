from abc import ABC, abstractmethod

'''
    Scraper abstract class
'''

class Scraper:
    def __init__(self, url) -> None:
        self.url = url

    @abstractmethod
    def get_problem(self):
        pass