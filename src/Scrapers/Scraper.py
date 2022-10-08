from abc import ABC, abstractmethod
import json
import os
import requests
from pathlib import Path
from ..Config.Config import Config
'''
    Scraper abstract class
'''

class Scraper:
    def __init__(self, url) -> None:
        self.url = url

    def __getResponse(self):
        # Because request only makes http request calls, change our https link to http
        protocol , link = self.url.split(':')
        protocol = 'http'
        url = protocol + ':'+link
        proxy = Config().get_proxy()
        response = requests.get(url,proxies = proxy,verify = False)
        return response

    @abstractmethod
    def get_problem(self):
        pass