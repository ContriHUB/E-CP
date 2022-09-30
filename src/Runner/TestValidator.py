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

    '''Function to validate output'''
    def validate_output(self):
        current_dir = os.listdir(self.dest)
        for expected_file in current_dir:
            if len(expected_file) >= 8 :
                if expected_file[:8] == 'expected' and expected_file[-4:] == '.txt':
                    for output_file in current_dir:
                        if len(output_file) >= 6 : 
                            if output_file[:6] == 'output' and output_file[-4:] == '.txt':
                                if expected_file[8:-4] == output_file[6:-4]:
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