'''
    Config related commands
'''

import click
from ..Config.Config import Config
from ..Runner.exceptions.UnsupportedLanguage import UnsupportedLanguage

@click.group()
def config():
    pass

@click.command()
@click.argument('lang', type=str)
def set_lang(lang):
    try:
        config = Config()
        config.set_lang(lang)
        click.echo(click.style(f'Language set to {lang}', fg='green'))

    except UnsupportedLanguage as e:
        click.echo(e)
    except Exception as e:
        click.echo(e)

@click.command()
@click.argument('path', type=str)
def set_temp(path):
    try:
        config = Config()
        config.set_template(path)
        click.echo(click.style('Template path set', fg='green'))
    except Exception as e:
        click.echo(e)

config.add_command(set_lang)
config.add_command(set_temp)