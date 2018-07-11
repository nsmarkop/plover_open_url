'''
Functionality to open URLs.
'''

import webbrowser


def open_url(_, url: str) -> None:
    '''
    Command to open a URL.

    :param _: The Plover engine that is executing the command.
    :type _: plover.engine.StenoEngine

    :param url: The URL to open. May also be a folder or file path.
    '''

    webbrowser.open(url)
