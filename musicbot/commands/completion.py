import click
import click_completion
import click_completion.core
from musicbot import helpers


@click.group(help="Shell completion", cls=helpers.GroupWithHelp)
def cli():
    pass


@cli.command(help='Show the click-completion-command completion code')
@click.option('-i', '--case-insensitive/--no-case-insensitive', help="Case insensitive completion")
@click.argument('shell', required=False, type=click_completion.DocumentedChoice(click_completion.core.shells))
def show(shell, case_insensitive):
    extra_env = {'_CLICK_COMPLETION_COMMAND_CASE_INSENSITIVE_COMPLETE': 'ON'} if case_insensitive else {}
    click.echo(click_completion.core.get_code(shell, extra_env=extra_env))


@cli.command(help='Install the click-completion-command completion')
@click.option('--append/--overwrite', help="Append the completion code to the file", default=None)
@click.option('-i', '--case-insensitive/--no-case-insensitive', help="Case insensitive completion")
@click.argument('shell', required=False, type=click_completion.DocumentedChoice(click_completion.core.shells))
@click.argument('path', required=False)
def install(append, case_insensitive, shell, path):
    extra_env = {'_CLICK_COMPLETION_COMMAND_CASE_INSENSITIVE_COMPLETE': 'ON'} if case_insensitive else {}
    shell, path = click_completion.core.install(shell=shell, path=path, append=append, extra_env=extra_env)
    click.echo(f'{shell} completion installed in {path}')
