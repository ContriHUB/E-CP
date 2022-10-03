'''
    CFScraper to handle codeforces problems
'''

import requests
from bs4 import BeautifulSoup
from requests.auth import HTTPProxyAuth
from .Scraper import Scraper
from ..Problem.Problem import Problem
from ..Problem.Test import Test

class CFScraper(Scraper):
    def __init__(self, url, proxy = "") -> None:
        super().__init__(url)
        auth = None
        user, password = "", ""
        if len(proxy)!=0:
            if proxy.find('@') != -1:
                auth , proxy = proxy.split('@')
            proxy = {
                "http":"http://"+proxy,
                "https":"https://"+proxy,
                "ftp":"ftp://"+proxy
                }
            if len(auth) != 0:
                user, password = auth.split(':')
        response = ""
        response = requests.get(url,proxies=proxy,auth = HTTPProxyAuth(user, password),verify=False)
        html_content = response.content
        self.soup = BeautifulSoup(html_content, 'lxml')

    def get_problem(self):
        problem = Problem(self.__find_problem_name(), self.__find_problem_tests())
        return problem

    def __find_problem_name(self):
        name_tag = self.soup.find('div', class_='title')
        name = name_tag.text
        return name

    def __find_problem_tests(self):
        input_tags = self.soup.find_all('div', class_='input')
        output_tags = self.soup.find_all('div', class_='output')
        tests = []

        length = len(input_tags)

        for index in range(length):
            input = input_tags[index].find('pre').text.strip()
            output = output_tags[index].find('pre').text.strip()
            tests.append(Test(input, output))
        
        return tests