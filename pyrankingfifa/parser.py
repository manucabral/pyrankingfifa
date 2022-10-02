'''
Table parser for FIFA ranking.
This module is used to parse the HTML table from the FIFA ranking page.
'''
from html.parser import HTMLParser


class TableParser(HTMLParser):
    '''Table parser class core. '''

    def __init__(self):
        '''Initializes the parser.'''
        super().__init__()
        self.__data = []
        self.__in_table = False

    def handle_starttag(self, tag: str, attrs: list) -> None:
        '''
        Handles the start tag.

        Args:
                tag (str): The tag.
                attrs (list): The attributes.
        '''
        if tag != 'table' or len(attrs) != 2 or attrs[0][1] != 'wikitable':
            return
        self.__in_table = True

    def handle_endtag(self, tag: str) -> None:
        '''
        Handles the end tag.

        Args:
                tag (str): The tag.
        '''
        if tag == 'table' and self.__in_table:
            self.__in_table = False

    def handle_data(self, data: str) -> None:
        '''
        Handles the data.

        Args:
                data (str): The data value.
        '''
        if self.__in_table and len(data.strip()) > 0:
            self.__data.append(data.strip())

    @property
    def data(self) -> list:
        '''
        Returns the data.

        Returns:
                list: The data.
        '''
        return self.__data
