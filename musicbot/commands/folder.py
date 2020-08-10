import logging
import json
import concurrent.futures as cf
import click
import enlighten
from prettytable import PrettyTable
from mutagen import MutagenError
from musicbot import helpers, lib
from musicbot.exceptions import MusicbotError
from musicbot.config import config
from musicbot.music.file import File, folder_option, checks_options

logger = logging.getLogger(__name__)


@click.group(help='Manage folders', cls=helpers.GroupWithHelp)
def cli():
    pass


@cli.command(help='List tracks')
@helpers.add_options(
    helpers.folders_argument +
    helpers.output_option
)
def tracks(folders, output):
    tracks = helpers.genfiles(folders)
    if output == 'json':
        tracks_dict = [{'title': t.title, 'artist': t.artist, 'album': t.album} for t in tracks]
        print(json.dumps(tracks_dict))
    elif output == 'table':
        pt = PrettyTable()
        pt.field_names = ["Track", "Title", "Artist", "Album"]
        for t in tracks:
            pt.add_row([t.number, t.title, t.artist, t.album])
        print(pt)
    else:
        raise NotImplementedError


@cli.command(help='Convert all files in folders to mp3')
@helpers.add_options(
    folder_option +
    helpers.folders_argument +
    helpers.concurrency_options +
    helpers.dry_option
)
def flac2mp3(folders, folder, concurrency, dry):
    flac_files = list(lib.find_files(folders, ['flac']))
    if not flac_files:
        logger.warning(f"No flac files detected in {folders}")
        return

    enabled = not config.quiet
    with enlighten.Manager(enabled=enabled) as manager:
        with manager.counter(total=len(flac_files), desc="converting musics") as pbar:
            with cf.ThreadPoolExecutor(max_workers=concurrency) as executor:
                def convert(flac_path):
                    try:
                        f = File(flac_path)
                        f.to_mp3(folder, dry)
                    except MusicbotError as e:
                        logger(e)
                    finally:
                        pbar.update()
                executor.shutdown = lambda wait: None
                futures = [executor.submit(convert, flac_path[1]) for flac_path in flac_files]
                cf.wait(futures)


@cli.command(aliases=['consistency'], help='Check music files consistency')
@helpers.add_options(
    helpers.folders_argument +
    helpers.dry_option +
    checks_options
)
def inconsistencies(folders, fix, **kwargs):
    musics = helpers.genfiles(folders)
    pt = PrettyTable()
    pt.field_names = ["Folder", "Path", "Inconsistencies"]
    for m in musics:
        try:
            if fix:
                m.fix(**kwargs)
            if m.inconsistencies:
                pt.add_row([m.folder, m.path, ', '.join(m.inconsistencies)])
        except (OSError, MutagenError):
            pt.add_row([m.folder, m.path, "could not open file"])
    print(pt)
