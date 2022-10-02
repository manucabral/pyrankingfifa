'''This module simulates a simple football team.'''


class Team:
    '''Team class core.'''

    def __init__(self, *args):
        '''Initialize the team.'''
        self.__date = args[0]
        self.__rank = int(args[1])
        self.__name = args[2]
        self.__points = float(args[3])

    def __str__(self) -> str:
        '''Return a string representation of the team.'''
        return f"Team(rank={self.rank}, name={self.name}, date={self.date})"

    def __repr__(self) -> str:
        '''Return a string representation of the team.'''
        return self.__str__()

    @property
    def rank(self) -> int:
        '''Return the rank of the team.'''
        return self.__rank

    @property
    def name(self) -> str:
        '''Return the name of the team.'''
        return self.__name

    @property
    def points(self) -> float:
        '''Return the points of the team.'''
        return self.__points

    @property
    def date(self) -> str:
        '''Return the date of the team.'''
        return self.__date
