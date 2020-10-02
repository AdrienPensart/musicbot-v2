import logging
import os
from typing import Optional
import click
import attr
from click_option_group import optgroup  # type: ignore
from click_skeleton import ExpandedPath
from musicbot import defaults
from musicbot.config import config
from musicbot.spotify import Spotify

logger = logging.getLogger(__name__)


def config_string_spotify(ctx: click.Context, param: click.Parameter, arg_value: str) -> Optional[str]:
    name = param.name
    value = None

    config_value = config.configfile.get('spotify', name, fallback=None)
    if config_value:
        value = config_value
        logger.info(f"{name} : config key loaded : {config_value}")

    name_upper = name.upper().replace('-', '_')
    env_name = 'MB_SPOTIFY_' + name_upper
    env_value = os.getenv(env_name, None)
    if env_value:
        value = env_value
        logger.info(f"{name} : env key {env_name} loaded : {env_value}")

    default_name = 'DEFAULT_' + name_upper
    default_value = globals().get(default_name, None)
    logger.info(f'{name} : default_name: {default_name} default_value: {default_value}')

    if arg_value and arg_value != default_value:
        logger.info(f"{name} : arg value loaded : {arg_value}")
        value = arg_value

    if not value:
        logger.info(f"{name} : default arg value loaded {default_name} : {arg_value}")
        value = default_value

    if env_value and arg_value and env_value != arg_value:
        logger.info(f"{name} : env value {env_value} is not sync with arg value {arg_value}")
    if env_value and config_value and env_value != config_value:
        logger.info(f"{name} : config value {config_value} is not sync with env value {env_value}")
    if arg_value and config_value and arg_value != config_value:
        logger.info(f"{name} : config value {config_value} is not sync with arg value {arg_value}")

    if not value and param.required:
        raise click.BadParameter(f'missing arg {param.name} or env {env_name} or {param.name} in [spotify] section of {config.config}', ctx, param, param.name)
    logger.info(f"{name} : final value {value}")
    return value


def sane_spotify(ctx: click.Context, param: click.Parameter, value: str) -> Spotify:
    spotify_params = {}
    ctx.params[param.name] = value
    for field in attr.fields_dict(Spotify):
        spotify_params[field] = ctx.params[field]
        ctx.params.pop(field)
    spotify = Spotify(**spotify_params)
    ctx.params['spotify'] = spotify
    return spotify


cache_path_option = optgroup.option(
    '--cache-path',
    help='Spotify cache path',
    is_eager=True,
    type=ExpandedPath(writable=True, readable=True, dir_okay=False),
    default=defaults.DEFAULT_CACHE_PATH,
    callback=config_string_spotify,
)

scope_option = optgroup.option(
    '--scope',
    help='Spotify OAuth scope',
    is_eager=True,
    default=defaults.DEFAULT_SCOPES,
    callback=config_string_spotify,
)

redirect_uri_option = optgroup.option(
    '--redirect-uri',
    help='Spotify redirect URI',
    is_eager=True,
    default=defaults.DEFAULT_REDIRECT_URI,
    callback=config_string_spotify,
)

username_option = optgroup.option(
    '--username',
    help='Spotify username',
    is_eager=True,
    callback=config_string_spotify,
)

client_id_option = optgroup.option(
    '--client-id',
    help='Spotify client ID',
    is_eager=True,
    callback=config_string_spotify,
)

client_secret_option = optgroup.option(
    '--client-secret',
    help='Spotify client secret',
    is_eager=True,
    callback=config_string_spotify,
)

token_option = optgroup.option(
    '--token',
    help='Spotify token',
    expose_value=False,
    callback=sane_spotify,
)

options = [
    optgroup.group('Spotify options'),
    username_option,
    client_id_option,
    client_secret_option,
    token_option,
    cache_path_option,
    scope_option,
    redirect_uri_option,
]