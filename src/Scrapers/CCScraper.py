'''
    CCScraper to handle CodeChef problems
'''

import requests
from bs4 import BeautifulSoup

from .Scraper import Scraper
from ..Problem.Problem import Problem
from ..Problem.Test import Test
import time

class CCScraper(Scraper):
    def __init__(self, url) -> None:
        super().__init__(url)
        response = self._Scraper__getResponse(is_dynamic=True)
        html_content = response
        self.soup = BeautifulSoup(html_content, 'lxml')

    def get_problem(self):
        problem = Problem(self.__find_problem_name(), self.__find_problem_tests())
        return problem

    def __find_problem_name(self):
        name_tag = self.soup.find('div', class_='_problem__title_bvg0e_488').find('span')
        name = name_tag.text
        return name

    def __find_problem_tests(self):
        input_tag = self.soup.find_all('div', class_='_values_lulsq_204')[0]
        output_tag = self.soup.find_all('div', class_='_values_lulsq_204')[1]
        tests = []

        input = "\n".join([x.text for x in input_tag.find('pre')])
        output = output_tag.find('pre').text.strip()
        tests.append(Test(input, output))
        
        return tests