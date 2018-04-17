'''
Functionality to open URLs with Plover commands.
'''

import webbrowser

from plover.engine import StenoEngine

def open_url(engine: StenoEngine, url: str) -> None:
    '''
    Command to open a URL with Plover.

    :param engine: The active Plover engine that is executing the command.
    :type engine: plover.engine.StenoEngine

    :param url: The URL to open.
    :type url: str
    '''

    webbrowser.open(url)
