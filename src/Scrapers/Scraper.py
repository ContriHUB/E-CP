from abc import ABC, abstractmethod
import json
import os
from pathlib import Path
'''
    Scraper abstract class
'''

class Scraper:
    def __init__(self, url) -> None:
        self.url = url

    @abstractmethod
    def get_problem(self):
        pass
    
    def get_proxy(self):
        config_file_path = config_file_path = Path(os.path.dirname(os.path.realpath(__file__)), '../Config/config.json')
        with open(config_file_path, 'r') as config_file:
            config = json.load(config_file)
        proxy =  config['proxy']
        proxy = {'http':'http://'+proxy,'https':'https://'+proxy}
        return proxy