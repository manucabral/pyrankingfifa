'''
Team implementation for pyrankingfifa package.
This module is used to represent a team in the FIFA ranking.
'''


class Team:
    '''Team class core.'''

    def __init__(self, rank: str, name: str, points: str):
        '''Initializes the team.'''
        self.__rank = int(rank)
        self.__name = name
        self.__points = float(points)

    def __str__(self):
        '''Returns the string representation of the team.'''
        return f'Team({self.__name})'

    @property
    def rank(self) -> int:
        '''Returns the rank.'''
        return self.__rank

    @property
    def name(self) -> str:
        '''Returns the name.'''
        return self.__name

    @property
    def points(self) -> float:
        '''Returns the points.'''
        return self.__points
