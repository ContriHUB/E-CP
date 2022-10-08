'''
    Validate expected and code output and print result
'''

import os
import click

class TestValidator:
    def __init__(self, dest) -> None:
        self.dest = dest

    '''Function to compare output'''
    def __compare_output(self, expected, output):
        expected_lines = expected.readlines()
        output_lines = output.readlines()

        match = (len(expected_lines) == len(output_lines))
    
        length = min(len(expected_lines), len(output_lines))
        for index in range(length):
            match &= (expected_lines[index] == output_lines[index])

        click.echo(click.style('Code output: ', fg='blue', bold=True))
        click.echo()

        for index in range(len(output_lines)):
            color = 'green'
            if index >= length:
                color = 'red'
            else :
                if output_lines[index] != expected_lines[index]:
                    color = 'red'
            
            click.echo(click.style(output_lines[index].rstrip(), bg=color, fg='white'))

        click.echo()
        click.echo(click.style('Expected output: ', fg='blue', bold=True))
        click.echo()

        for index in range(len(expected_lines)):
            color = 'green'
            if index >= length:
                color = 'red'
            else :
                if output_lines[index] != expected_lines[index]:
                    color = 'red'
            
            click.echo(click.style(expected_lines[index].rstrip(), bg=color, fg='white'))    

        return match       

    '''Function to show output if expected output file is not present'''
    def __show_output(self, output):
        output_lines = output.readlines()
        click.echo(click.style('Code output: ', fg='blue', bold=True))
        click.echo()
    
        for index in range(len(output_lines)):
            click.echo(click.style(output_lines[index].rstrip(), bg='green', fg='white'))

        click.echo()

    '''Function to validate output'''
    def validate_output(self):
        current_dir = os.listdir(self.dest)
        for output_file in current_dir:
            if len(output_file) >= 6 : 
                if output_file[:6] == 'output' and output_file[-4:] == '.txt':
                    expected_file = 'expected' + output_file[6:]
                    if expected_file in current_dir:
                        click.echo(click.style(output_file[6:-4], fg='blue'))
                        click.echo()
                        with open(expected_file) as expected:
                            with open(output_file) as output:
                                result = self.__compare_output(expected, output)
                                click.echo()
                                if result:
                                    click.echo(click.style('AC', bg='green'))
                                else :
                                    click.echo(click.style('WA', bg='red'))
                                click.echo()
                    else:
                        click.echo(click.style('There is no expected output file, do you wish to continue? (y/N)', fg='red'))
                        choice = input()
                        if choice == 'y':
                            click.echo(click.style(output_file[6:-4], fg='blue'))
                            click.echo()
                            with open(output_file) as output:
                                self.__show_output(output)
                        else:
                            click.echo(click.style('Code execution stopped for input_{}.txt as there is no expected output file'.format(output_file[7:-4]), fg='red', bold=True))
                            click.echo()