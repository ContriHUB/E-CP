import os
import click
import subprocess
from pathlib import Path
from .Runner import Runner
from ..exceptions.CodeError import CodeError

'''
    Class to handle C++ code execution
'''
class CppRunner(Runner):
    def __init__(self, dest, code_file) -> None:
        super().__init__(dest, code_file)
        self.exec_file = self.__compile_code()

    def __compile_code(self):
        return subprocess.run(['g++', self.code_file, '-o', 'a'], capture_output=True, text=True)

    def __execute_code(self, exec_file, stdin = None):
        return subprocess.run([exec_file], capture_output=True, text=True, stdin=stdin)

    def run_on_test_files(self):
        current_dir = os.listdir(self.dest)

        for file_name in current_dir:
            if len(file_name) >= 5:
                if file_name[:5] == 'input' and file_name[-4:] == '.txt':
                    input_file_name = file_name
                    
                    input_file_path = Path(input_file_name)
                    with open(input_file_path, 'r') as content:   
                        # Run executable file with sample input files
                        exec_result = self.__execute_code('./a', content)

                        if exec_result.returncode != 0:
                            raise CodeError(exec_result.stderr, 'runtime error', exec_result.returncode)

                        output_file_path = Path(f'output{file_name[5:]}')

                        # Write output obtained from to output_file
                        with open(output_file_path, 'w') as output_file:
                            output_file.write(exec_result.stdout.strip()) 

    def run_on_custom(self):
        exec_result = self.__execute_code(Path(self.dest, 'a'))
        click.echo(exec_result.stdout)
