import os
import click
import subprocess
from pathlib import Path
from .Runner import Runner
from ..exceptions import CodeError

'''
    Class to handlle python code execution
'''
class PythonRunner(Runner):
    def __init__(self, dest, code_file) -> None:
        super().__init__(dest, code_file)
    
    def __execute_code(self, stdin = subprocess.PIPE):
        return subprocess.run(['python', 'code.py'], capture_output=True, text=True, stdin=stdin)

    def run_on_test_files(self):
        current_dir = os.listdir(self.dest)

        for file_name in current_dir:
            if len(file_name) >= 5:
                if file_name[:5] == 'input' and file_name[-4:] == '.txt':
                    input_file_name = file_name
                    
                    input_file_path = Path(input_file_name)
                    with open(input_file_path, 'r') as content:   
                        # Run executable file with sample input files
                        exec_result = self.__execute_code(content)

                        if exec_result.returncode != 0:
                            raise CodeError(exec_result.stderr, 'runtime error', exec_result.returncode)

                        output_file_path = Path(f'output{file_name[5:]}')

                        # Write output obtained from to output_file
                        with open(output_file_path, 'w') as output_file:
                            output_file.write(exec_result.stdout.strip()) 
    
    def run_on_custom(self):
        exec_result = self.__execute_code()
        click.echo(exec_result.stdout)
