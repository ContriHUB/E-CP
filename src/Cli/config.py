'''
    Config related commands
'''

import click, requests
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

@click.command()
@click.argument('proxy', type=str)
def set_proxy(proxy):
    try:
        config = Config()
        config.set_proxy(proxy)
        click.echo(click.style('Proxy set to '+proxy, fg='green'))
    except Exception as e:
        click.echo(e)

@click.command()
def remove_proxy():
    try:
        config = Config()
        config.remove_proxy()
        click.echo(click.style('Proxy removed sucessfully.', fg='green'))
    except Exception as e:
        click.echo(e)
config.add_command(set_lang)
config.add_command(set_temp)
config.add_command(set_proxy)
config.add_command(remove_proxy)