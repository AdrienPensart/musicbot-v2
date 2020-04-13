import logging
import os
import codecs
import csv
import json
import datetime
from shutil import copyfile
from textwrap import indent
import click
from tqdm import tqdm
from prettytable import PrettyTable
from musicbot import helpers, user
from musicbot.lib import bytes_to_human, find_files, all_files, empty_dirs, except_directories
from musicbot.music import mfilter
from musicbot.player import play
from musicbot.playlist import print_playlist
from musicbot.config import config
from musicbot.music.file import supported_formats


logger = logging.getLogger(__name__)


@click.group(help='''Local music management''', cls=helpers.GroupWithHelp)
def cli():
    pass


@cli.command(help='''List artists''')
@helpers.add_options(user.auth_options + helpers.output_option)
def artists(user, output):
    if output == 'table':
        pt = PrettyTable()
        pt.field_names = ["Name"]
        for a in user.artists:
            pt.add_row([a['name']])
        print(pt)
    elif output == 'json':
        print(json.dumps(user.artists))
    else:
        raise NotImplementedError


@cli.command(help='''Raw query''')
@click.argument('query')
@helpers.add_options(user.auth_options)
def execute(user, query):
    print(json.dumps(user._post(query)['data']))


@cli.command()
@helpers.add_options(user.auth_options)
def load_filters(user):
    '''Load default filters'''
    user.load_default_filters()


@cli.command(help='''List filters''')
@helpers.add_options(user.auth_options + helpers.output_option)
def filters(user, output):
    if output == 'json':
        print(json.dumps(user.filters))
    elif output == 'table':
        pt = PrettyTable()
        pt.field_names = ["Name", "Keywords", "No keywords", "Min rating", "Max rating"]
        for f in user.filters:
            pt.add_row([f['name'], f['keywords'], f['noKeywords'], f['minRating'], f['maxRating']])
        print(pt)
    else:
        raise NotImplementedError


@cli.command('filter', help='''Print a filter''')
@helpers.add_options(user.auth_options + helpers.output_option)
@click.argument('name')
def _filter(user, name, output):
    f = user.filter(name)
    if output == 'json':
        print(json.dumps(f))
    elif output == 'table':
        print(f)
    else:
        raise NotImplementedError


@cli.command(help='''Generate some stats for music collection with filters''')
@helpers.add_options(user.auth_options + helpers.output_option + mfilter.options)
def stats(user, output, **kwargs):
    mf = mfilter.Filter(**kwargs)
    stats = user.do_stat(mf)
    if output == 'json':
        print(json.dumps(stats))
    elif output == 'table':
        pt = PrettyTable()
        pt.field_names = ["Stat", "Value"]
        pt.add_row(["Music", stats['musics']])
        pt.add_row(["Artist", stats['artists']])
        pt.add_row(["Album", stats['albums']])
        pt.add_row(["Genre", stats['genres']])
        pt.add_row(["Keywords", stats['keywords']])
        pt.add_row(["Size", bytes_to_human(int(stats['size']))])
        pt.add_row(["Total duration", datetime.timedelta(seconds=int(stats['duration']))])
        print(pt)
    else:
        raise NotImplementedError


@cli.command(help='''List folders''')
@helpers.add_options(user.auth_options + helpers.output_option)
def folders(user, output):
    _folders = user.folders
    if output == 'json':
        print(json.dumps(_folders))
    elif output == 'table':
        pt = PrettyTable()
        pt.field_names = ["Folder"]
        for f in _folders:
            pt.add_row([f])
        print(pt)
    else:
        raise NotImplementedError


@cli.command(help='''(re)Load musics''')
@helpers.add_options(user.auth_options + helpers.folders_argument)
def scan(user, folders):
    if not folders:
        folders = user.folders
    files = helpers.genfiles(folders)
    user.bulk_insert(files)


@cli.command(help='''Just list music files''')
@helpers.add_options(user.auth_options + helpers.folders_argument)
def find(user, folders):
    if not folders:
        folders = user.folders

    files = find_files(folders, supported_formats)
    for f in files:
        print(f[1])


@cli.command(help='''Watch files changes in folders''')
@helpers.add_options(user.auth_options)
def watch(user):
    user.watch()


@cli.command(help='''Clean all musics''')
@helpers.add_options(user.auth_options)
def clean(user):
    user.clean_musics()


@cli.command(help='''Copy selected musics with filters to destination folder''')
@helpers.add_options(user.auth_options + helpers.dry_option + mfilter.options)
@click.argument('destination')
def sync(user, dry, destination, **kwargs):
    logger.info('Destination: %s', destination)
    mf = mfilter.Filter(**kwargs)
    musics = user.do_filter(mf)

    files = list(all_files(destination))
    logger.info(f"Files : {len(files)}")
    if not files:
        logger.warning("No files found in destination")

    destinations = {f[len(destination) + 1:]: f for f in files}
    logger.info(f"Destinations : {len(destinations)}")
    sources = {m['path'][len(m['folder']) + 1:]: m['path'] for m in musics}
    logger.info(f"Sources : {len(sources)}")
    to_delete = set(destinations.keys()) - set(sources.keys())
    logger.info(f"To delete: {len(to_delete)}")
    if to_delete:
        with tqdm(total=len(to_delete), disable=config.quiet) as pbar:
            for d in to_delete:
                pbar.set_description(f"Deleting musics and playlists: {os.path.basename(destinations[d])}")
                if not dry:
                    try:
                        logger.info("Deleting %s", destinations[d])
                        os.remove(destinations[d])
                    except OSError as e:
                        logger.error(e)
                else:
                    logger.info("[DRY-RUN] False Deleting %s", destinations[d])
                pbar.update(1)

    to_copy = set(sources.keys()) - set(destinations.keys())
    logger.info(f"To copy: {len(to_copy)}")
    if to_copy:
        with tqdm(total=len(to_copy), disable=config.quiet) as pbar:
            for c in sorted(to_copy):
                final_destination = os.path.join(destination, c)
                try:
                    pbar.set_description(f'Copying {os.path.basename(sources[c])} to {destination}')
                    if not dry:
                        logger.info("Copying %s to %s", sources[c], final_destination)
                        os.makedirs(os.path.dirname(final_destination), exist_ok=True)
                        copyfile(sources[c], final_destination)
                    else:
                        logger.info("[DRY-RUN] False Copying %s to %s", sources[c], final_destination)
                    pbar.update(1)
                except KeyboardInterrupt:
                    logger.debug(f"Cleanup {final_destination}")
                    os.remove(final_destination)
                    raise

    import shutil
    for d in empty_dirs(destination):
        if any(e in d for e in except_directories):
            logger.debug(f"Invalid path {d}")
            continue
        if not dry:
            shutil.rmtree(d)
        logger.info("[DRY-RUN] Removing empty dir %s", d)


@cli.command(help='''Check music files consistency''')
@helpers.add_options(user.auth_options + helpers.folders_argument)
def consistency(user, folders):
    if not folders:
        folders = user.folders

    musics = helpers.genfiles(folders)
    pt = PrettyTable()
    pt.field_names = ["Inconsistency", "File"]
    for m in musics:
        try:
            if m.path.endswith('.flac'):
                if m.comment and not m.description:
                    pt.add_row(['Comment (' + m.comment + ') used in flac', m.path])
            if m.path.endswith('.mp3'):
                if m.description and not m.comment:
                    pt.add_row(['Description (' + m.description + ') used in mp3 : ', m.path])
            if not m.title:
                pt.add_row(["No title  : '" + m.title + "' on ", m.path])
            filename = os.path.basename(m.path)
            if filename == f"{str(m.number).zfill(2)} - {m.title}.mp3":
                continue
            if filename == f"{str(m.number).zfill(2)} - {m.title}.flac":
                continue
            pt.add_row([f"Invalid title format, '{filename}' should start by '{str(m.number).zfill(2)} - {m.title}'", m.path])
            if m.artist not in m.path:
                pt.add_row(["Artist invalid : " + m.artist + " is not in ", m.path])
            if m.genre == '':
                pt.add_row(["No genre : ", m.path])
            if m.album == '':
                pt.add_row(["No album : ", m.path])
            if m.artist == '':
                pt.add_row(["No artist : ", m.path])
            if m.rating == 0.0:
                pt.add_row(["No rating : ", m.path])
            if m.number == -1:
                pt.add_row(["Invalid track number : ", m.path])
        except OSError:
            pt.add_row(["Could not open file : ", m.path])
    print(pt)


@cli.command(help='''Generate a new playlist''')
@helpers.add_options(user.auth_options + helpers.dry_option + mfilter.options + helpers.output_option)
@click.argument('path', type=click.File('w'), default='-')
def playlist(user, output, path, dry, **kwargs):
    mf = mfilter.Filter(**kwargs)
    if output == 'm3u':
        p = user.playlist(mf)
        if not dry:
            print(p, file=path)
        else:
            logger.info('DRY RUN: Writing playlist to %s with content:\n%s', path, p)
    else:
        tracks = user.do_filter(mf)
        if output == 'json':
            print(json.dumps(tracks), file=path)
        elif output == 'table':
            print_playlist(tracks, path)
        elif output == 'csv':
            folders = user.folders
            logger.info('Scanning folders: %s', folders)
            files = helpers.genfiles(folders)

            musicwriter = csv.writer(path, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for f in files:
                musicwriter.writerow(f.ordered_dict().values())


@cli.command(help='''Generate bests playlists with some rules''')
@helpers.add_options(user.auth_options + helpers.dry_option + mfilter.options)
@click.argument('path', type=click.Path(exists=True))
@click.option('--prefix', envvar='MB_PREFIX', help="Append prefix before each path (implies relative)", default='')
@click.option('--suffix', envvar='MB_SUFFIX', help="Append this suffix to playlist name", default='')
def bests(user, dry, path, prefix, suffix, **kwargs):
    if prefix:
        kwargs['relative'] = True
        if not prefix.endswith('/'):
            prefix += '/'
    mf = mfilter.Filter(**kwargs)
    playlists = user.bests(mf)
    with tqdm(total=len(playlists), disable=config.quiet) as pbar:
        for p in playlists:
            playlist_filepath = os.path.join(path, p['name'] + suffix + '.m3u')
            pbar.set_description(f"Best playlist {prefix} {suffix}: {os.path.basename(playlist_filepath)}")
            content = indent(p['content'], prefix, lambda line: line != '#EXTM3U\n')
            if not dry:
                try:
                    with codecs.open(playlist_filepath, 'w', "utf-8-sig") as playlist_file:
                        logger.debug('Writing playlist to %s with content:\n%s', playlist_filepath, content)
                        playlist_file.write(content)
                except (FileNotFoundError, LookupError, ValueError, UnicodeError) as e:
                    logger.warning(f'Unable to write playlist to {playlist_filepath} because of {e}')
            else:
                logger.info('DRY RUN: Writing playlist to %s with content:\n%s', playlist_filepath, content)
            pbar.update(1)


@cli.command(help='Music player', aliases=['play'])
@helpers.add_options(user.auth_options + mfilter.options)
def player(user, **kwargs):
    mf = mfilter.Filter(**kwargs)
    tracks = user.do_filter(mf)
    play(tracks)
