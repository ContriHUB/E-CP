'''
    Problem related commands
'''

from pathlib import Path
import click
import os
from ..Scrapers.CFScraper import CFScraper
from ..Problem.ProblemManager import ProblemManager

@click.command()
@click.argument('url', type=str)
@click.argument('dest', type=str, default='.')
def problem(dest, url):
    try:
        scraper = CFScraper(url)
        problem = scraper.get_problem()

        # Create directory
        dir = Path(dest, problem.name)

        # If directory is not already created
        if(not dir.exists()):
            os.mkdir(dir)

        problem_manager = ProblemManager(dir, problem)

        # Create test files
        problem_manager.create_test_files()
        
        # Create code file
        problem_manager.create_code_file()

        click.echo(click.style('Problem created successfully', fg='green'))
    except Exception as e:
        click.echo(e)