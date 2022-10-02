'''This module contains all the exceptions used in PyRankingFifa.'''


class RankingError(Exception):
    '''Raise when an error occurs in the ranking.'''


class RankingDateError(Exception):
    '''Raise when the date error occurs.'''


class ParserError(Exception):
    '''Raise when the parsing error occurs.'''
