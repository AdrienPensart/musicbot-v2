import time
import re
import os
import logging
import string
import random
import functools
import enlighten
import click
from click_help_colors import HelpColorsGroup
from click_didyoumean import DYMGroup
from click_aliases import ClickAliasedGroup
from .config import config
from .lib import seconds_to_human, find_files, filecount
from .music.file import File, supported_formats

logger = logging.getLogger(__name__)

DEFAULT_MB_CONCURRENCY = 8
concurrency_options = [
    click.option(
        '--concurrency',
        help='Number of coroutines',
        default=DEFAULT_MB_CONCURRENCY,
        show_default=True
    )
]

DEFAULT_DRY = False
dry_option = [
    click.option(
        '--dry',
        help='Take no real action',
        default=DEFAULT_DRY,
        is_flag=True,
        show_default=True
    )
]

DEFAULT_SAVE = False
save_option = [
    click.option(
        '--save', '-s',
        help='Save to config file',
        default=DEFAULT_SAVE,
        is_flag=True,
        show_default=True
    )
]

DEFAULT_MB_OUTPUT = 'table'
output_option = [
    click.option(
        '--output',
        help='Output format',
        default=DEFAULT_MB_OUTPUT,
        show_default=True,
        type=click.Choice(['table', 'json'])
    )
]
playlist_output_option = [
    click.option(
        '--output',
        help='Output format',
        default=DEFAULT_MB_OUTPUT,
        show_default=True,
        type=click.Choice(['json', 'm3u', 'table'])
    )
]

Red = "\033[0;31;40m"
Green = "\033[0;32;40m"
Yellow = "\033[0;33;40m"
Reset = "\033[0m"


def strip_colors(text):
    ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
    return ansi_escape.sub('', text)


def random_password(size=8):
    alphabet = string.ascii_letters + string.digits
    return ''.join(random.choice(alphabet) for i in range(size))


class GroupWithHelp(DYMGroup, ClickAliasedGroup, HelpColorsGroup):
    def __init__(self, *args, **kwargs):
        kwargs['help_headers_color'] = 'yellow'
        kwargs['help_options_color'] = 'green'
        super().__init__(*args, **kwargs)

        @click.command('help')
        @click.argument('command', required=False)
        @click.pass_context
        def _help(ctx, command):
            '''Print help'''
            if command:
                argument = command[0]
                c = self.get_command(ctx, argument)
                print(c.get_help(ctx))
            else:
                print(ctx.parent.get_help())
        self.add_command(_help)


def timeit(f):
    @functools.wraps(f)
    def wrapper(*args, **params):
        start = time.time()
        result = f(*args, **params)
        for_human = seconds_to_human(time.time() - start)
        if config.timings:
            logger.info(f'TIMINGS {f.__name__}: {for_human}')
        return result
    return wrapper


def add_options(options):
    def _add_options(func):
        for option in reversed(options):
            func = option(func)
        return func
    return _add_options


def config_string(ctx, param, value):
    arg_value = value
    logger.info(f"{param.name} : try loading with value : {value}")

    config_value = config.configfile.get('musicbot', param.name, fallback=None)
    logger.info(f"{param.name} : try loading with config key : {config_value}")

    if arg_value:
        value = arg_value

    if config_value:
        if not value or value == param.default:
            value = config_value
        elif arg_value and arg_value != config_value:
            logger.warning(f"{param.name} : config value {config_value} is not sync with arg value {arg_value}")

    if not value and param.required:
        raise click.BadParameter(f'missing arg or config {param.name} in {config.config}', ctx, param.name, param.name)
    logger.info(f"{param.name} : final value {value}")
    ctx.params[param.name] = value
    return ctx.params[param.name]


def config_list(ctx, param, value):
    arg_value = value
    logger.info(f"{param.name} : try loading with value : {value}")

    config_value = config.configfile.get('musicbot', param.name, fallback=None)
    if config_value is not None:
        config_value = tuple(config_value.split(','))
    logger.info(f"{param.name} : try loading with config key : {config_value}")

    if arg_value:
        value = arg_value

    if config_value:
        if not value or value == param.default:
            value = config_value
        elif arg_value and arg_value != config_value:
            logger.warning(f"{param.name} : config value {config_value} is not sync with arg value {arg_value}")

    if not value and param.required:
        raise click.BadParameter(f'missing arg or config {param.name} in {config.config}', ctx, param.name, param.name)
    logger.info(f"{param.name} : final value {value}")
    ctx.params[param.name] = value
    return ctx.params[param.name]


@timeit
def genfiles(folders):
    directories = [os.path.abspath(f) for f in folders]
    enabled = directories and not config.quiet
    with enlighten.Manager(enabled=enabled) as manager:
        count = 0
        with manager.counter(total=len(directories), desc=f"Music counting {folders}") as pbar:
            for directory in directories:
                try:
                    pbar.desc = f"Music counting {directory}"
                    subcount = filecount(directory, supported_formats)
                    logger.info(f"{directory} : file count: {subcount}")
                    count += subcount
                finally:
                    pbar.update()
        files = []
        enabled = count and not config.quiet
        with manager.counter(total=count, desc="Music listing", enabled=enabled) as pbar:
            file_list = find_files(folders, supported_formats)
            music_files = list(file_list)
            for f in music_files:
                try:
                    m = File(f[1], f[0])
                    files.append(m)
                except OSError as e:
                    logger.error(e)
                finally:
                    pbar.update()
    return files

folders_argument = [
    click.argument('folders', nargs=-1, callback=config_list, type=click.Path(exists=True, file_okay=False))
]
