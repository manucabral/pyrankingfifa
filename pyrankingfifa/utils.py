'''
    Utilities for the pyrankingfifa package.
    This module is used to provide some utilities for the package.
'''
from urllib.request import urlopen


def request(url: str) -> str:
    '''
    Request the url and return the response as a string.

    Args:
        url (str): The url to request.
    Raises:
        Exception: If the request fails.
    Returns:
        str: The response as a string.
    '''
    try:
        with urlopen(url) as response:
            return response.read().decode()
    except Exception as exc:
        raise exc
