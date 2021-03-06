
Commands
--------
.. code-block::

  Usage: musicbot [OPTIONS] COMMAND [ARGS]...

    Music swiss knife, new gen.

  Options:
    Global options: 
      -c, --config FILE              Config file path  [default: ~/musicbot.ini]
      -l, --log FILE                 Log file path  [default: ]
      -q, --quiet                    Disable progress bars  [default: False]
      -t, --timings                  Set verbosity to info and show execution timings  [default: False]
    Verbosity: [mutually_exclusive]
      --debug                        Debug verbosity
      --info                         Info verbosity
      --warning                      Warning verbosity
      --error                        Error verbosity
      --critical                     Critical verbosity
    -V, --version                    Show the version and exit.
    -h, --help                       Show this message and exit.

  Commands:
    completion    Shell completion
    filter        Filter management
    folder        Manage folders
    help          Print help
    local         Local music management
    music (file)  Music file
    readme (doc)  Generates a README.rst
    spotify       Spotify tool
    user          User management
    version       Print version
    youtube       Youtube tool

musicbot completion
*******************
.. code-block::

  Usage: musicbot completion [OPTIONS] COMMAND [ARGS]...

    Shell completion subcommand

  Options:
    -h, --help  Show this message and exit.

  Commands:
    help                   Print help
    install                Install the click-completion-command completion
    show (generate,print)  Show the click-completion-command completion code

musicbot completion install
***************************
.. code-block::

  Usage: musicbot completion install [OPTIONS] [[bash|fish|zsh|powershell]] [PATH]

    Auto install shell completion code in your rc file

  Options:
    -i, --case-insensitive  Case insensitive completion
    --append / --overwrite  Append the completion code to the file
    -h, --help              Show this message and exit.

musicbot completion show
************************
.. code-block::

  Usage: musicbot completion show [OPTIONS] [[bash|fish|zsh|powershell]]

    Generate shell code to enable completion

  Options:
    -i, --case-insensitive  Case insensitive completion
    -h, --help              Show this message and exit.

musicbot filter
***************
.. code-block::

  Usage: musicbot filter [OPTIONS] COMMAND [ARGS]...

    Filter management

  Options:
    -h, --help  Show this message and exit.

  Commands:
    count             Count filters
    delete (remove)   Delete a filter
    help              Print help
    list              List filters
    load              Load default filters
    show (get,print)  Print a filter

musicbot filter count
*********************
.. code-block::

  Usage: musicbot filter count [OPTIONS]

    Count filters

  Options:
    Auth options: 
      -g, --graphql TEXT   GraphQL endpoint  [default: http://127.0.0.1:5000/graphql]
      -t, --token TEXT     User token
      -e, --email TEXT     User email
      -p, --password TEXT  User password
    -h, --help             Show this message and exit.

musicbot filter delete
**********************
.. code-block::

  Usage: musicbot filter delete [OPTIONS] NAME

    Delete a filter

  Options:
    Auth options: 
      -g, --graphql TEXT   GraphQL endpoint  [default: http://127.0.0.1:5000/graphql]
      -t, --token TEXT     User token
      -e, --email TEXT     User email
      -p, --password TEXT  User password
    -h, --help             Show this message and exit.

musicbot filter list
********************
.. code-block::

  Usage: musicbot filter list [OPTIONS]

    List filters

  Options:
    --output [json|table|m3u]  Output format  [default: table]
    Auth options: 
      -g, --graphql TEXT       GraphQL endpoint  [default: http://127.0.0.1:5000/graphql]
      -t, --token TEXT         User token
      -e, --email TEXT         User email
      -p, --password TEXT      User password
    -h, --help                 Show this message and exit.

musicbot filter load
********************
.. code-block::

  Usage: musicbot filter load [OPTIONS]

    Load default filters

  Options:
    Auth options: 
      -g, --graphql TEXT   GraphQL endpoint  [default: http://127.0.0.1:5000/graphql]
      -t, --token TEXT     User token
      -e, --email TEXT     User email
      -p, --password TEXT  User password
    -h, --help             Show this message and exit.

musicbot filter show
********************
.. code-block::

  Usage: musicbot filter show [OPTIONS] NAME

    Print a filter

  Options:
    --output [json|table|m3u]  Output format  [default: table]
    Auth options: 
      -g, --graphql TEXT       GraphQL endpoint  [default: http://127.0.0.1:5000/graphql]
      -t, --token TEXT         User token
      -e, --email TEXT         User email
      -p, --password TEXT      User password
    -h, --help                 Show this message and exit.

musicbot folder
***************
.. code-block::

  Usage: musicbot folder [OPTIONS] COMMAND [ARGS]...

    Manage folders

  Options:
    -h, --help  Show this message and exit.

  Commands:
    add-keywords                   Add keywords to music
    delete-keywords                Delete keywords to music
    find                           Just list music files
    flac2mp3                       Convert all files in folders to mp3
    help                           Print help
    inconsistencies (consistency)  Check music files consistency
    playlist (tracks)              Generate a playlist
    tags                           Print music tags

musicbot folder add-keywords
****************************
.. code-block::

  Usage: musicbot folder add-keywords [OPTIONS] FOLDER [KEYWORDS]...

    Add keywords to music

  Options:
    --dry       Take no real action  [default: False]
    -h, --help  Show this message and exit.

musicbot folder delete-keywords
*******************************
.. code-block::

  Usage: musicbot folder delete-keywords [OPTIONS] FOLDER [KEYWORDS]...

    Delete keywords to music

  Options:
    --dry       Take no real action  [default: False]
    -h, --help  Show this message and exit.

musicbot folder find
********************
.. code-block::

  Usage: musicbot folder find [OPTIONS] [FOLDERS]...

    Just list music files

  Options:
    -h, --help  Show this message and exit.

musicbot folder flac2mp3
************************
.. code-block::

  Usage: musicbot folder flac2mp3 [OPTIONS] [FOLDERS]...

    Convert all files in folders to mp3

  Options:
    --folder DIRECTORY     Destination folder
    --concurrency INTEGER  Number of coroutines  [default: 8]
    --dry                  Take no real action  [default: False]
    --flat                 Do not create subfolders
    -h, --help             Show this message and exit.

musicbot folder inconsistencies
*******************************
.. code-block::

  Usage: musicbot folder inconsistencies [OPTIONS] [FOLDERS]...

    Check music files consistency

  Options:
    --dry                                               Take no real action  [default: False]
    Check options: 
      --checks [no-title|no-artist|no-album|no-genre|no-rating|no-tracknumber|invalid-title|invalid-comment|invalid-path]
                                                        Consistency tests  [default: no-title, no-artist, no-album, no-genre, no-rating, no-
                                                        tracknumber, invalid-title, invalid-comment, invalid-path]
      --fix                                             Fix musics
    -h, --help                                          Show this message and exit.

musicbot folder playlist
************************
.. code-block::

  Usage: musicbot folder playlist [OPTIONS] [FOLDERS]...

    Generate a playlist

  Options:
    --output [json|table|m3u]  Output format  [default: table]
    Ordering options: 
      --shuffle                Randomize selection
      --interleave             Interleave tracks by artist
    -h, --help                 Show this message and exit.

musicbot folder tags
********************
.. code-block::

  Usage: musicbot folder tags [OPTIONS] [FOLDERS]...

    Print music tags

  Options:
    -h, --help  Show this message and exit.

musicbot help
*************
.. code-block::

  Usage: musicbot help [OPTIONS]

    Print help

  Options:
    -h, --help  Show this message and exit.

musicbot local
**************
.. code-block::

  Usage: musicbot local [OPTIONS] COMMAND [ARGS]...

    Local music management

  Options:
    -h, --help  Show this message and exit.

  Commands:
    bests                          Generate bests playlists with some rules
    clean                          Clean all musics
    count                          Count musics
    execute (fetch,query)          Raw query
    folders                        List folders
    help                           Print help
    inconsistencies (consistency)  Check music consistency
    player (play)                  Music player
    playlist (tracks)              Generate a new playlist
    rescan                         Clean and load musics
    scan                           Load musics
    stats (stat)                   Generate some stats for music collection with filters
    sync                           Copy selected musics with filters to destination folder
    watch                          Watch files changes in folders

musicbot local bests
********************
.. code-block::

  Usage: musicbot local bests [OPTIONS] FOLDER

    Generate bests playlists with some rules

  Options:
    --prefix TEXT             Append prefix before each path (implies relative)
    --suffix TEXT             Append this suffix to playlist name
    --dry                     Take no real action  [default: False]
    Auth options: 
      -g, --graphql TEXT      GraphQL endpoint  [default: http://127.0.0.1:5000/graphql]
      -t, --token TEXT        User token
      -e, --email TEXT        User email
      -p, --password TEXT     User password
    Filter options: 
      --name TEXT             Filter name
      --limit INTEGER         Fetch a maximum limit of music
      --youtubes TEXT         Select musics with a youtube link
      --no-youtubes TEXT      Select musics without youtube link
      --spotifys TEXT         Select musics with a spotifys link
      --no-spotifys TEXT      Select musics without spotifys link
      --formats TEXT          Select musics with file format
      --no-formats TEXT       Filter musics without format
      --keywords TEXT         Select musics with keywords
      --no-keywords TEXT      Filter musics without keywords
      --artists TEXT          Select musics with artists
      --no-artists TEXT       Filter musics without artists
      --albums TEXT           Select musics with albums
      --no-albums TEXT        Filter musics without albums
      --titles TEXT           Select musics with titles
      --no-titles TEXT        Filter musics without titless
      --genres TEXT           Select musics with genres
      --no-genres TEXT        Filter musics without genres
      --min-duration INTEGER  Minimum duration filter (hours:minutes:seconds)
      --max-duration INTEGER  Maximum duration filter (hours:minutes:seconds))
      --min-size INTEGER      Minimum file size filter (in bytes)
      --max-size INTEGER      Maximum file size filter (in bytes)
      --min-rating FLOAT      Minimum rating  [default: 0.0]
      --max-rating FLOAT      Maximum rating  [default: 5.0]
      --relative              Generate relatives paths
      --shuffle               Randomize selection
    Ordering options: 
      --shuffle               Randomize selection
    -h, --help                Show this message and exit.

musicbot local clean
********************
.. code-block::

  Usage: musicbot local clean [OPTIONS]

    Clean all musics

  Options:
    Auth options: 
      -g, --graphql TEXT   GraphQL endpoint  [default: http://127.0.0.1:5000/graphql]
      -t, --token TEXT     User token
      -e, --email TEXT     User email
      -p, --password TEXT  User password
    -y, --yes              Confirm action
    -h, --help             Show this message and exit.

musicbot local count
********************
.. code-block::

  Usage: musicbot local count [OPTIONS]

    Count musics

  Options:
    Auth options: 
      -g, --graphql TEXT   GraphQL endpoint  [default: http://127.0.0.1:5000/graphql]
      -t, --token TEXT     User token
      -e, --email TEXT     User email
      -p, --password TEXT  User password
    -h, --help             Show this message and exit.

musicbot local execute
**********************
.. code-block::

  Usage: musicbot local execute [OPTIONS] QUERY

    Raw query

  Options:
    Auth options: 
      -g, --graphql TEXT   GraphQL endpoint  [default: http://127.0.0.1:5000/graphql]
      -t, --token TEXT     User token
      -e, --email TEXT     User email
      -p, --password TEXT  User password
    -h, --help             Show this message and exit.

musicbot local folders
**********************
.. code-block::

  Usage: musicbot local folders [OPTIONS]

    List folders

  Options:
    --output [json|table|m3u]  Output format  [default: table]
    Auth options: 
      -g, --graphql TEXT       GraphQL endpoint  [default: http://127.0.0.1:5000/graphql]
      -t, --token TEXT         User token
      -e, --email TEXT         User email
      -p, --password TEXT      User password
    -h, --help                 Show this message and exit.

musicbot local inconsistencies
******************************
.. code-block::

  Usage: musicbot local inconsistencies [OPTIONS]

    Check music consistency

  Options:
    Check options: 
      --checks [no-title|no-artist|no-album|no-genre|no-rating|no-tracknumber|invalid-title|invalid-comment|invalid-path]
                                                        Consistency tests  [default: no-title, no-artist, no-album, no-genre, no-rating, no-
                                                        tracknumber, invalid-title, invalid-comment, invalid-path]
      --fix                                             Fix musics
    --dry                                               Take no real action  [default: False]
    Auth options: 
      -g, --graphql TEXT                                GraphQL endpoint  [default: http://127.0.0.1:5000/graphql]
      -t, --token TEXT                                  User token
      -e, --email TEXT                                  User email
      -p, --password TEXT                               User password
    Filter options: 
      --name TEXT                                       Filter name
      --limit INTEGER                                   Fetch a maximum limit of music
      --youtubes TEXT                                   Select musics with a youtube link
      --no-youtubes TEXT                                Select musics without youtube link
      --spotifys TEXT                                   Select musics with a spotifys link
      --no-spotifys TEXT                                Select musics without spotifys link
      --formats TEXT                                    Select musics with file format
      --no-formats TEXT                                 Filter musics without format
      --keywords TEXT                                   Select musics with keywords
      --no-keywords TEXT                                Filter musics without keywords
      --artists TEXT                                    Select musics with artists
      --no-artists TEXT                                 Filter musics without artists
      --albums TEXT                                     Select musics with albums
      --no-albums TEXT                                  Filter musics without albums
      --titles TEXT                                     Select musics with titles
      --no-titles TEXT                                  Filter musics without titless
      --genres TEXT                                     Select musics with genres
      --no-genres TEXT                                  Filter musics without genres
      --min-duration INTEGER                            Minimum duration filter (hours:minutes:seconds)
      --max-duration INTEGER                            Maximum duration filter (hours:minutes:seconds))
      --min-size INTEGER                                Minimum file size filter (in bytes)
      --max-size INTEGER                                Maximum file size filter (in bytes)
      --min-rating FLOAT                                Minimum rating  [default: 0.0]
      --max-rating FLOAT                                Maximum rating  [default: 5.0]
      --relative                                        Generate relatives paths
      --shuffle                                         Randomize selection
    Ordering options: 
      --shuffle                                         Randomize selection
    -h, --help                                          Show this message and exit.

musicbot local player
*********************
.. code-block::

  Usage: musicbot local player [OPTIONS]

    Music player

  Options:
    Auth options: 
      -g, --graphql TEXT      GraphQL endpoint  [default: http://127.0.0.1:5000/graphql]
      -t, --token TEXT        User token
      -e, --email TEXT        User email
      -p, --password TEXT     User password
    Filter options: 
      --name TEXT             Filter name
      --limit INTEGER         Fetch a maximum limit of music
      --youtubes TEXT         Select musics with a youtube link
      --no-youtubes TEXT      Select musics without youtube link
      --spotifys TEXT         Select musics with a spotifys link
      --no-spotifys TEXT      Select musics without spotifys link
      --formats TEXT          Select musics with file format
      --no-formats TEXT       Filter musics without format
      --keywords TEXT         Select musics with keywords
      --no-keywords TEXT      Filter musics without keywords
      --artists TEXT          Select musics with artists
      --no-artists TEXT       Filter musics without artists
      --albums TEXT           Select musics with albums
      --no-albums TEXT        Filter musics without albums
      --titles TEXT           Select musics with titles
      --no-titles TEXT        Filter musics without titless
      --genres TEXT           Select musics with genres
      --no-genres TEXT        Filter musics without genres
      --min-duration INTEGER  Minimum duration filter (hours:minutes:seconds)
      --max-duration INTEGER  Maximum duration filter (hours:minutes:seconds))
      --min-size INTEGER      Minimum file size filter (in bytes)
      --max-size INTEGER      Maximum file size filter (in bytes)
      --min-rating FLOAT      Minimum rating  [default: 0.0]
      --max-rating FLOAT      Maximum rating  [default: 5.0]
      --relative              Generate relatives paths
      --shuffle               Randomize selection
    Ordering options: 
      --shuffle               Randomize selection
    -h, --help                Show this message and exit.

musicbot local playlist
***********************
.. code-block::

  Usage: musicbot local playlist [OPTIONS]

    Generate a new playlist

  Options:
    --output [json|table|m3u]  Output format  [default: table]
    Auth options: 
      -g, --graphql TEXT       GraphQL endpoint  [default: http://127.0.0.1:5000/graphql]
      -t, --token TEXT         User token
      -e, --email TEXT         User email
      -p, --password TEXT      User password
    Filter options: 
      --name TEXT              Filter name
      --limit INTEGER          Fetch a maximum limit of music
      --youtubes TEXT          Select musics with a youtube link
      --no-youtubes TEXT       Select musics without youtube link
      --spotifys TEXT          Select musics with a spotifys link
      --no-spotifys TEXT       Select musics without spotifys link
      --formats TEXT           Select musics with file format
      --no-formats TEXT        Filter musics without format
      --keywords TEXT          Select musics with keywords
      --no-keywords TEXT       Filter musics without keywords
      --artists TEXT           Select musics with artists
      --no-artists TEXT        Filter musics without artists
      --albums TEXT            Select musics with albums
      --no-albums TEXT         Filter musics without albums
      --titles TEXT            Select musics with titles
      --no-titles TEXT         Filter musics without titless
      --genres TEXT            Select musics with genres
      --no-genres TEXT         Filter musics without genres
      --min-duration INTEGER   Minimum duration filter (hours:minutes:seconds)
      --max-duration INTEGER   Maximum duration filter (hours:minutes:seconds))
      --min-size INTEGER       Minimum file size filter (in bytes)
      --max-size INTEGER       Maximum file size filter (in bytes)
      --min-rating FLOAT       Minimum rating  [default: 0.0]
      --max-rating FLOAT       Maximum rating  [default: 5.0]
      --relative               Generate relatives paths
      --shuffle                Randomize selection
    Ordering options: 
      --shuffle                Randomize selection
      --interleave             Interleave tracks by artist
    -h, --help                 Show this message and exit.

musicbot local rescan
*********************
.. code-block::

  Usage: musicbot local rescan [OPTIONS] [FOLDERS]...

    Clean and load musics

  Options:
    Auth options: 
      -g, --graphql TEXT   GraphQL endpoint  [default: http://127.0.0.1:5000/graphql]
      -t, --token TEXT     User token
      -e, --email TEXT     User email
      -p, --password TEXT  User password
    -h, --help             Show this message and exit.

musicbot local scan
*******************
.. code-block::

  Usage: musicbot local scan [OPTIONS] [FOLDERS]...

    Load musics

  Options:
    -s, --save             Save to config file  [default: False]
    Auth options: 
      -g, --graphql TEXT   GraphQL endpoint  [default: http://127.0.0.1:5000/graphql]
      -t, --token TEXT     User token
      -e, --email TEXT     User email
      -p, --password TEXT  User password
    -h, --help             Show this message and exit.

musicbot local stats
********************
.. code-block::

  Usage: musicbot local stats [OPTIONS]

    Generate some stats for music collection with filters

  Options:
    --output [json|table|m3u]  Output format  [default: table]
    Auth options: 
      -g, --graphql TEXT       GraphQL endpoint  [default: http://127.0.0.1:5000/graphql]
      -t, --token TEXT         User token
      -e, --email TEXT         User email
      -p, --password TEXT      User password
    Filter options: 
      --name TEXT              Filter name
      --limit INTEGER          Fetch a maximum limit of music
      --youtubes TEXT          Select musics with a youtube link
      --no-youtubes TEXT       Select musics without youtube link
      --spotifys TEXT          Select musics with a spotifys link
      --no-spotifys TEXT       Select musics without spotifys link
      --formats TEXT           Select musics with file format
      --no-formats TEXT        Filter musics without format
      --keywords TEXT          Select musics with keywords
      --no-keywords TEXT       Filter musics without keywords
      --artists TEXT           Select musics with artists
      --no-artists TEXT        Filter musics without artists
      --albums TEXT            Select musics with albums
      --no-albums TEXT         Filter musics without albums
      --titles TEXT            Select musics with titles
      --no-titles TEXT         Filter musics without titless
      --genres TEXT            Select musics with genres
      --no-genres TEXT         Filter musics without genres
      --min-duration INTEGER   Minimum duration filter (hours:minutes:seconds)
      --max-duration INTEGER   Maximum duration filter (hours:minutes:seconds))
      --min-size INTEGER       Minimum file size filter (in bytes)
      --max-size INTEGER       Maximum file size filter (in bytes)
      --min-rating FLOAT       Minimum rating  [default: 0.0]
      --max-rating FLOAT       Maximum rating  [default: 5.0]
      --relative               Generate relatives paths
      --shuffle                Randomize selection
    Ordering options: 
      --shuffle                Randomize selection
    -h, --help                 Show this message and exit.

musicbot local sync
*******************
.. code-block::

  Usage: musicbot local sync [OPTIONS] DESTINATION

    Copy selected musics with filters to destination folder

  Options:
    --dry                     Take no real action  [default: False]
    -y, --yes                 Confirm action
    Auth options: 
      -g, --graphql TEXT      GraphQL endpoint  [default: http://127.0.0.1:5000/graphql]
      -t, --token TEXT        User token
      -e, --email TEXT        User email
      -p, --password TEXT     User password
    Filter options: 
      --name TEXT             Filter name
      --limit INTEGER         Fetch a maximum limit of music
      --youtubes TEXT         Select musics with a youtube link
      --no-youtubes TEXT      Select musics without youtube link
      --spotifys TEXT         Select musics with a spotifys link
      --no-spotifys TEXT      Select musics without spotifys link
      --formats TEXT          Select musics with file format
      --no-formats TEXT       Filter musics without format
      --keywords TEXT         Select musics with keywords
      --no-keywords TEXT      Filter musics without keywords
      --artists TEXT          Select musics with artists
      --no-artists TEXT       Filter musics without artists
      --albums TEXT           Select musics with albums
      --no-albums TEXT        Filter musics without albums
      --titles TEXT           Select musics with titles
      --no-titles TEXT        Filter musics without titless
      --genres TEXT           Select musics with genres
      --no-genres TEXT        Filter musics without genres
      --min-duration INTEGER  Minimum duration filter (hours:minutes:seconds)
      --max-duration INTEGER  Maximum duration filter (hours:minutes:seconds))
      --min-size INTEGER      Minimum file size filter (in bytes)
      --max-size INTEGER      Maximum file size filter (in bytes)
      --min-rating FLOAT      Minimum rating  [default: 0.0]
      --max-rating FLOAT      Maximum rating  [default: 5.0]
      --relative              Generate relatives paths
      --shuffle               Randomize selection
    Ordering options: 
      --shuffle               Randomize selection
    --flat                    Do not create subfolders
    --delete                  Delete files on destination if not present in library
    -h, --help                Show this message and exit.

musicbot local watch
********************
.. code-block::

  Usage: musicbot local watch [OPTIONS]

    Watch files changes in folders

  Options:
    Auth options: 
      -g, --graphql TEXT   GraphQL endpoint  [default: http://127.0.0.1:5000/graphql]
      -t, --token TEXT     User token
      -e, --email TEXT     User email
      -p, --password TEXT  User password
    -h, --help             Show this message and exit.

musicbot music
**************
.. code-block::

  Usage: musicbot music [OPTIONS] COMMAND [ARGS]...

    Music file

  Options:
    -h, --help  Show this message and exit.

  Commands:
    add-keywords                       Add keywords to music
    delete-keywords (remove-keywords)  Delete keywords to music
    fingerprint                        Print music fingerprint
    flac2mp3                           Convert flac music to mp3
    help                               Print help
    inconsistencies (consistency)      Check music consistency
    set-tags                           Set music title
    tags                               Print music tags

musicbot music add-keywords
***************************
.. code-block::

  Usage: musicbot music add-keywords [OPTIONS] PATH [KEYWORDS]...

    Add keywords to music

  Options:
    --dry       Take no real action  [default: False]
    -h, --help  Show this message and exit.

musicbot music delete-keywords
******************************
.. code-block::

  Usage: musicbot music delete-keywords [OPTIONS] PATH [KEYWORDS]...

    Delete keywords to music

  Options:
    --dry       Take no real action  [default: False]
    -h, --help  Show this message and exit.

musicbot music fingerprint
**************************
.. code-block::

  Usage: musicbot music fingerprint [OPTIONS] PATH

    Print music fingerprint

  Options:
    --acoustid-api-key TEXT  AcoustID API Key
    -h, --help               Show this message and exit.

musicbot music flac2mp3
***********************
.. code-block::

  Usage: musicbot music flac2mp3 [OPTIONS] PATH

    Convert flac music to mp3

  Options:
    --folder DIRECTORY  Destination folder
    --dry               Take no real action  [default: False]
    -h, --help          Show this message and exit.

musicbot music inconsistencies
******************************
.. code-block::

  Usage: musicbot music inconsistencies [OPTIONS] PATH

    Check music consistency

  Options:
    --folder DIRECTORY                                  Destination folder
    --dry                                               Take no real action  [default: False]
    Check options: 
      --checks [no-title|no-artist|no-album|no-genre|no-rating|no-tracknumber|invalid-title|invalid-comment|invalid-path]
                                                        Consistency tests  [default: no-title, no-artist, no-album, no-genre, no-rating, no-
                                                        tracknumber, invalid-title, invalid-comment, invalid-path]
      --fix                                             Fix musics
    -h, --help                                          Show this message and exit.

musicbot music set-tags
***********************
.. code-block::

  Usage: musicbot music set-tags [OPTIONS] PATH

    Set music title

  Options:
    --dry              Take no real action  [default: False]
    Music options: 
      --keywords TEXT  Keywords
      --artist TEXT    Artist
      --album TEXT     Album
      --title TEXT     Title
      --genre TEXT     Genre
      --number TEXT    Track number
      --rating TEXT    Rating
    -h, --help         Show this message and exit.

musicbot music tags
*******************
.. code-block::

  Usage: musicbot music tags [OPTIONS] PATH

    Print music tags

  Options:
    -h, --help  Show this message and exit.

musicbot readme
***************
.. code-block::

  Usage: musicbot readme [OPTIONS]

    Generates a complete readme

  Options:
    --output [rst|markdown]  README output format  [default: rst]
    -h, --help               Show this message and exit.

musicbot spotify
****************
.. code-block::

  Usage: musicbot spotify [OPTIONS] COMMAND [ARGS]...

    Spotify tool

  Options:
    -h, --help  Show this message and exit.

  Commands:
    cached-token      Token informations
    diff              Diff between local and spotify
    help              Print help
    new-token (auth)  Generate a new token
    playlist          Show playlist
    playlists         List playlists
    refresh-token     Get a new token
    tracks            Show tracks

musicbot spotify cached-token
*****************************
.. code-block::

  Usage: musicbot spotify cached-token [OPTIONS]

    Token informations

  Options:
    Spotify options: 
      --spotify-token TEXT          Spotify token
      --spotify-username TEXT       Spotify username
      --spotify-client-id TEXT      Spotify client ID
      --spotify-client-secret TEXT  Spotify client secret
      --spotify-cache-path FILE     Spotify cache path
      --spotify-scope TEXT          Spotify OAuth scopes, comma separated
      --spotify-redirect-uri TEXT   Spotify redirect URI
    -h, --help                      Show this message and exit.

musicbot spotify diff
*********************
.. code-block::

  Usage: musicbot spotify diff [OPTIONS]

    Diff between local and spotify

  Options:
    Auth options: 
      -g, --graphql TEXT            GraphQL endpoint  [default: http://127.0.0.1:5000/graphql]
      -t, --token TEXT              User token
      -e, --email TEXT              User email
      -p, --password TEXT           User password
    Spotify options: 
      --spotify-token TEXT          Spotify token
      --spotify-username TEXT       Spotify username
      --spotify-client-id TEXT      Spotify client ID
      --spotify-client-secret TEXT  Spotify client secret
      --spotify-cache-path FILE     Spotify cache path
      --spotify-scope TEXT          Spotify OAuth scopes, comma separated
      --spotify-redirect-uri TEXT   Spotify redirect URI
    Filter options: 
      --name TEXT                   Filter name
      --limit INTEGER               Fetch a maximum limit of music
      --youtubes TEXT               Select musics with a youtube link
      --no-youtubes TEXT            Select musics without youtube link
      --spotifys TEXT               Select musics with a spotifys link
      --no-spotifys TEXT            Select musics without spotifys link
      --formats TEXT                Select musics with file format
      --no-formats TEXT             Filter musics without format
      --keywords TEXT               Select musics with keywords
      --no-keywords TEXT            Filter musics without keywords
      --artists TEXT                Select musics with artists
      --no-artists TEXT             Filter musics without artists
      --albums TEXT                 Select musics with albums
      --no-albums TEXT              Filter musics without albums
      --titles TEXT                 Select musics with titles
      --no-titles TEXT              Filter musics without titless
      --genres TEXT                 Select musics with genres
      --no-genres TEXT              Filter musics without genres
      --min-duration INTEGER        Minimum duration filter (hours:minutes:seconds)
      --max-duration INTEGER        Maximum duration filter (hours:minutes:seconds))
      --min-size INTEGER            Minimum file size filter (in bytes)
      --max-size INTEGER            Maximum file size filter (in bytes)
      --min-rating FLOAT            Minimum rating  [default: 0.0]
      --max-rating FLOAT            Maximum rating  [default: 5.0]
      --relative                    Generate relatives paths
      --shuffle                     Randomize selection
    Ordering options: 
      --shuffle                     Randomize selection
    --output [json|table|m3u]       Output format  [default: table]
    --download-playlist             Create the download playlist
    --min-threshold FLOAT RANGE     Minimum distance threshold  [0<=x<=100]
    --max-threshold FLOAT RANGE     Maximum distance threshold  [0<=x<=100]
    -h, --help                      Show this message and exit.

musicbot spotify new-token
**************************
.. code-block::

  Usage: musicbot spotify new-token [OPTIONS]

    Generate a new token

  Options:
    Spotify options: 
      --spotify-token TEXT          Spotify token
      --spotify-username TEXT       Spotify username
      --spotify-client-id TEXT      Spotify client ID
      --spotify-client-secret TEXT  Spotify client secret
      --spotify-cache-path FILE     Spotify cache path
      --spotify-scope TEXT          Spotify OAuth scopes, comma separated
      --spotify-redirect-uri TEXT   Spotify redirect URI
    -h, --help                      Show this message and exit.

musicbot spotify playlist
*************************
.. code-block::

  Usage: musicbot spotify playlist [OPTIONS] NAME

    Show playlist

  Options:
    Spotify options: 
      --spotify-token TEXT          Spotify token
      --spotify-username TEXT       Spotify username
      --spotify-client-id TEXT      Spotify client ID
      --spotify-client-secret TEXT  Spotify client secret
      --spotify-cache-path FILE     Spotify cache path
      --spotify-scope TEXT          Spotify OAuth scopes, comma separated
      --spotify-redirect-uri TEXT   Spotify redirect URI
    --output [json|table|m3u]       Output format  [default: table]
    -h, --help                      Show this message and exit.

musicbot spotify playlists
**************************
.. code-block::

  Usage: musicbot spotify playlists [OPTIONS]

    List playlists

  Options:
    Spotify options: 
      --spotify-token TEXT          Spotify token
      --spotify-username TEXT       Spotify username
      --spotify-client-id TEXT      Spotify client ID
      --spotify-client-secret TEXT  Spotify client secret
      --spotify-cache-path FILE     Spotify cache path
      --spotify-scope TEXT          Spotify OAuth scopes, comma separated
      --spotify-redirect-uri TEXT   Spotify redirect URI
    -h, --help                      Show this message and exit.

musicbot spotify refresh-token
******************************
.. code-block::

  Usage: musicbot spotify refresh-token [OPTIONS]

    Get a new token

  Options:
    Spotify options: 
      --spotify-token TEXT          Spotify token
      --spotify-username TEXT       Spotify username
      --spotify-client-id TEXT      Spotify client ID
      --spotify-client-secret TEXT  Spotify client secret
      --spotify-cache-path FILE     Spotify cache path
      --spotify-scope TEXT          Spotify OAuth scopes, comma separated
      --spotify-redirect-uri TEXT   Spotify redirect URI
    -h, --help                      Show this message and exit.

musicbot spotify tracks
***********************
.. code-block::

  Usage: musicbot spotify tracks [OPTIONS]

    Show tracks

  Options:
    Spotify options: 
      --spotify-token TEXT          Spotify token
      --spotify-username TEXT       Spotify username
      --spotify-client-id TEXT      Spotify client ID
      --spotify-client-secret TEXT  Spotify client secret
      --spotify-cache-path FILE     Spotify cache path
      --spotify-scope TEXT          Spotify OAuth scopes, comma separated
      --spotify-redirect-uri TEXT   Spotify redirect URI
    --output [json|table|m3u]       Output format  [default: table]
    -h, --help                      Show this message and exit.

musicbot user
*************
.. code-block::

  Usage: musicbot user [OPTIONS] COMMAND [ARGS]...

    User management

  Options:
    -h, --help  Show this message and exit.

  Commands:
    help                        Print help
    list                        List users (admin)
    login (token)               Authenticate user
    register (add,create,new)   Register a new user
    unregister (delete,remove)  Remove a user

musicbot user list
******************
.. code-block::

  Usage: musicbot user list [OPTIONS]

    List users (admin)

  Options:
    --output [json|table|m3u]        Output format  [default: table]
    Admin options: 
      --graphql-admin TEXT           GraphQL endpoint  [default: http://127.0.0.1:5001/graphql]
    Basic auth: [all_or_none]
      --graphql-admin-user TEXT      GraphQL admin user (basic auth)
      --graphql-admin-password TEXT  GraphQL admin password (basic auth)
    -h, --help                       Show this message and exit.

musicbot user login
*******************
.. code-block::

  Usage: musicbot user login [OPTIONS]

    Authenticate user

  Options:
    -s, --save             Save to config file  [default: False]
    Login options: 
      -g, --graphql TEXT   GraphQL endpoint  [default: http://127.0.0.1:5000/graphql]
      -e, --email TEXT     User email
      -p, --password TEXT  User password
    -h, --help             Show this message and exit.

musicbot user register
**********************
.. code-block::

  Usage: musicbot user register [OPTIONS]

    Register a new user

  Options:
    -s, --save             Save to config file  [default: False]
    Register options: 
      -g, --graphql TEXT   GraphQL endpoint  [default: http://127.0.0.1:5000/graphql]
      -e, --email TEXT     User email
      -p, --password TEXT  User password
      --first-name TEXT    User first name
      --last-name TEXT     User last name
    -h, --help             Show this message and exit.

musicbot user unregister
************************
.. code-block::

  Usage: musicbot user unregister [OPTIONS]

    Remove a user

  Options:
    Auth options: 
      -g, --graphql TEXT   GraphQL endpoint  [default: http://127.0.0.1:5000/graphql]
      -t, --token TEXT     User token
      -e, --email TEXT     User email
      -p, --password TEXT  User password
    -h, --help             Show this message and exit.

musicbot version
****************
.. code-block::

  Usage: musicbot version [OPTIONS]

    Print version, equivalent to -V and --version

  Options:
    -h, --help  Show this message and exit.

musicbot youtube
****************
.. code-block::

  Usage: musicbot youtube [OPTIONS] COMMAND [ARGS]...

    Youtube tool

  Options:
    -h, --help  Show this message and exit.

  Commands:
    download     Download a youtube link with artist and title
    find         Search a youtube link with artist and title
    fingerprint  Fingerprint a youtube video
    help         Print help
    search       Search a youtube link with artist and title

musicbot youtube download
*************************
.. code-block::

  Usage: musicbot youtube download [OPTIONS] ARTIST TITLE

    Download a youtube link with artist and title

  Options:
    --path TEXT
    -h, --help   Show this message and exit.

musicbot youtube find
*********************
.. code-block::

  Usage: musicbot youtube find [OPTIONS] PATH

    Search a youtube link with artist and title

  Options:
    --acoustid-api-key TEXT  AcoustID API Key
    -h, --help               Show this message and exit.

musicbot youtube fingerprint
****************************
.. code-block::

  Usage: musicbot youtube fingerprint [OPTIONS] URL

    Fingerprint a youtube video

  Options:
    --acoustid-api-key TEXT  AcoustID API Key
    -h, --help               Show this message and exit.

musicbot youtube search
***********************
.. code-block::

  Usage: musicbot youtube search [OPTIONS] ARTIST TITLE

    Search a youtube link with artist and title

  Options:
    -h, --help  Show this message and exit.
