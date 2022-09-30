from pathlib import Path
from .Problem import Problem
from ..Runner.mapper import ext_map
from ..Runner.exceptions.UnsupportedLanguage import UnsupportedLanguage
from ..Config.Config import Config

'''
    Class to manage current problem
'''
class ProblemManager:
    def __init__(self, dir, problem:Problem) -> None:
        self.dir = dir
        self.problem = problem

    
    '''Helper function to create test files'''
    def create_test_files(self):
        dir = self.dir
        tests = self.problem.tests

        index = 1
        for test in tests:
            input_test_file = Path(dir, f'input_{index}.txt')
            with open(input_test_file, 'w') as file:
                file.write(test.input)
            
            output_test_file = Path(dir, f'expected_{index}.txt')
            with open(output_test_file, 'w') as file:
                file.write(test.output)

            index += 1
    
        
    '''Helper function to create code file'''
    def create_code_file(self):
        dir = self.dir

        config = Config()
        lang = config.get_lang()
        if lang not in ext_map:
            raise UnsupportedLanguage(lang)

        code_file_path = Path(dir, f'code.{ext_map[lang]}')
        
        ''' 
            'w' with overwrite the file, even if we don't write anything 
            https://stackoverflow.com/questions/16208206/confused-by-python-file-mode-w#:~:text=w%2B-,Opens%20a%20file%20for%20both%20writing%20and%20reading.,file%20for%20reading%20and%20writing.
        '''
        with open(code_file_path, 'a') as code_file:
            template_path = config.get_template_path()
            try:
                with open(template_path, 'r') as template:
                    for line in template:
                        code_file.write(line)
            # OSError occurs when file cannot be opened
            except OSError as e:
                pass
            # Re-raise error if some other error occurred
            except Exception as e:
                raise