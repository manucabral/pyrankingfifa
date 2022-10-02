from pyrankingfifa.utils import Utilities
from pyrankingfifa.exceptions import ParserError


class Parser:
    '''Parser class core.'''

    def __init__(self, content: str, category: str):
        '''Initialize the parser.'''
        if not content or not category:
            raise ParserError('Content or category is empty.')
        self.__content = content
        self.__category = category
        self.__data = []

    @property
    def __parse_mens(self) -> list:
        '''Parse the content for the mens category.'''
        for row in Utilities.findall('<tr>(.*?)</tr>', self.__content):
            data = Utilities.findall(
                '<tr>(.*?)</tr>|title=("[^"]*"|[^,]*)|<td>(.*?)</td>', row)
            if len(data) < 6:
                continue
            rank, name = data[0][2], data[1][1].replace('"', '')
            points = data[2][2]
            self.__data += [(rank, name, points)]

    @property
    def __parse_womens(self) -> list:
        '''Parse the content for the womens category.'''

    def parse(self) -> list:
        '''
        Parse the content.

        Returns:
            list: A list of parsed data.
        '''
        action = {
            'mens': self.__parse_mens,
            'womens': self.__parse_womens
        }
        return action[self.__category]

    @property
    def data(self) -> list:
        '''Return the parsed data.'''
        return self.__data
