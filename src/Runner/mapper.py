'''
    Mappers to map functions and extensions to their respective handlers
'''

from .runner import run_cpp_code, run_python_code

runner_map = {
    'cpp' : run_cpp_code,
    'python' : run_python_code
}

ext_map = {
    'cpp' : 'cpp', 
    'python' : 'py'
}