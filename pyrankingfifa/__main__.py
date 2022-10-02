'''
Ranking class implementation.
This class is used to get the ranking of the FIFA World Cup.
'''
from pyrankingfifa.team import Team
from pyrankingfifa.utils import request
from pyrankingfifa.parser import TableParser


class Ranking:
    '''
    Ranking class core.
    This class is used to get the ranking of the FIFA World Cup.
    
    Args:
            use_cache (bool): If the data should be cached.
    '''

    __URL = 'https://en.wikipedia.org/wiki/FIFA_World_Rankings'

    def __init__(self, use_cache: bool = True):
        ''' Initializes the ranking. '''
        self.__use_cache = use_cache
        self.__raw_data = self.__get_data

    @property
    def __get_data(self) -> list:
        ''' Returns the raw data. '''
        return request(self.__URL)

    def __parse_data(self, data: list) -> list:
        ''' Parses the data. '''
        parser = TableParser()
        parser.feed(data)
        parsed = parser.data
        parsed.pop(1)
        return parsed

    def teams(self) -> list:
        '''
        Get first 20 teams of the ranking.
        Returns:
                list: The list of teams.
        Raises:
                ValueError: If the data is not valid.
        '''
        raw_data = self.__raw_data if self.__use_cache else self.__get_data
        data = self.__parse_data(raw_data)
        teams, points = data[::3][2:][:-1], data[1::3][2:]
        if len(teams) != len(points):
            raise ValueError('The number of teams and points are different.')
        return [Team(i+1, teams[i], points[i]) for i in range(len(teams))]
