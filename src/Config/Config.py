import json
import os
import requests
from pathlib import Path
from ..Runner.exceptions.UnsupportedLanguage import UnsupportedLanguage

'''
    Class to manage config related commands
'''
class UsernameNotFound(Exception):
    def __init__(self, msg):
        super().__init__(self, msg)

class Config():
    supported_lang = ['cpp', 'python', 'java']

    def __init__(self) -> None:
        self.config_file_path = self.get_config_path()

    def get_config_path(self) -> Path:
        config_file_path = Path(os.path.dirname(os.path.realpath(__file__)), 'config.json')
        return config_file_path

    def get_lang(self):
        config_file_path = self.config_file_path
    
        with open(config_file_path, 'r') as config_file:
            config = json.load(config_file)
        
        return config['language']

    def __is_lang_supported(self, lang):
        return lang in self.supported_lang

    def set_lang(self, lang):
        if(not self.__is_lang_supported(lang)):
            raise UnsupportedLanguage(lang)

        with open(self.config_file_path, 'r+') as config_file:
            config = json.load(config_file)
            config['language'] = lang
            config_file.seek(0)
            config_file.truncate()
            config_file.write(json.dumps(config))

    def set_template(self, temp_path):
        abs_path = os.path.abspath(temp_path)
        with open(self.config_file_path, 'r+') as config_file:
            config = json.load(config_file)
            config['template'] = abs_path
            config_file.seek(0)
            config_file.truncate()
            config_file.write(json.dumps(config))

    def get_template_path(self):
        config_file_path = self.config_file_path
    
        with open(config_file_path, 'r') as config_file:
            config = json.load(config_file)
        
        return config['template']

    def is_text_file(self, file_name):
        try:
            with open(file_name, 'tr') as check_file:
                check_file.read()
                return True
        except:
            return False

    def set_proxy(self, address):
        with open(self.config_file_path, 'r+') as config_file:
            config = json.load(config_file)
            config['proxy'] = address
            config_file.seek(0)
            config_file.truncate()
            config_file.write(json.dumps(config))

    def get_proxy(self):
        with open(self.config_file_path, 'r') as config_file:
            config = json.load(config_file)
        proxy =  config['proxy']
        if len(proxy)==0:
            proxy = {'http':None,'https':None}
        else:
            proxy = {'http':'http://'+proxy,'https':'https://'+proxy}
        return proxy
    
    def remove_proxy(self):
        with open(self.config_file_path, 'r+') as config_file:
            config = json.load(config_file)
            config['proxy'] = ""
            config_file.seek(0)
            config_file.truncate()
            config_file.write(json.dumps(config))

    def set_user(self, user):
        response = requests.get(url='http://codeforces.com/api/user.info?handles='+user,proxies=self.get_proxy())
        if(response.status_code!=200):
            raise UsernameNotFound('User not found')
        html_content = response.json()
        config_file_path = self.config_file_path
        with open(config_file_path, 'r+') as config_file:
            config = json.load(config_file)
            config["user"]["firstname"] = html_content["result"][0]["firstName"]
            config["user"]["lastname"] = html_content["result"][0]["lastName"]
            config["user"]["rating"] = str(html_content["result"][0]["rating"]),
            config["user"]["contri"] = str(html_content["result"][0]["contribution"]),
            config["user"]["rank"] = str(html_content["result"][0]["rank"]),
            config["user"]["maxrating"] = str(html_content["result"][0]["maxRating"])
            config_file.seek(0)
            config_file.truncate()
            config_file.write(json.dumps(config))
    
    def get_user(self):
        config_file_path = self.config_file_path
        with open(config_file_path, 'r') as config_file:
            config = json.load(config_file)
        return config["user"]