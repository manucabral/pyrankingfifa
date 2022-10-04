'''}
This module implements the core of the library.
Not all heavy lifting is done here, check the utils and parser modules.
'''
from pyrankingfifa.team import Team
from pyrankingfifa.parser import Parser
from pyrankingfifa.utils import Utilities
from pyrankingfifa.exceptions import RankingDateError, RankingError


class Ranking:
    '''
    Ranking class core.

    Attributes:
        category (str): Use 'mens' or 'womens'.
    '''

    def __init__(self, category: str):
        '''Initialize the ranking.'''
        if not self.__check_category(category):
            raise RankingError(f'Category {category} is not valid.')
        self.__category = category

    def __str__(self):
        '''Return a string representation of the ranking.'''
        return f"Ranking(category={self.category})"

    def __repr__(self):
        '''Return a string representation of the ranking.'''
        return self.__str__

    @property
    def __available_dates(self) -> list:
        '''
        Return a list of available dates to get the ranking.

        Returns:
            list: A list of available dates to get the ranking.
        '''
        url = Utilities.ENDPOINT['fifa'][self.__category]
        response = Utilities.request(url).decode('utf-8')
        values = Utilities.findall('"dates":\[(.*?)\]', response)
        dates = Utilities.findall('"text":"(.*?)"', values[0])
        # remove days because there are no more than 1 ranking per month
        dates = [date.split(' ', 1)[1].lower() for date in dates]
        return dates

    def __check_category(self, category: str) -> bool:
        '''
        Check if the category is valid.

        Args:
            category (str): The category to check.
        Returns:
            bool: True if the category is valid, False otherwise.
        '''
        # TODO: add 'womens' category
        return category in ['mens']  # , 'womens']

    @property
    def category(self) -> str:
        '''Return the category of the ranking.'''
        return self.__category

    def check_date(self, month: str, year: int) -> bool:
        '''
        Check if the date is available to get the ranking.

        Args:
            month (str): The month of the ranking, e.g. 'Jan', 'Feb', etc.
            year (int): The year of the ranking.
        Returns:
            bool: True if the date is available, False otherwise.
        '''
        # ceroacero website only saves rankings since 2007
        if int(year) < 2007:
            return False
        return f"{month} {year}".lower() in self.__available_dates

    def check_page(self, page: int) -> bool:
        '''
        Check if the page is valid.

        Args:
            page (int): The page to check.
        Returns:
            bool: True if the page is valid, False otherwise.
        '''
        return page > 0 and page <= 11

    def __download(self, filename: str, month: str, year: int, page: int) -> str:
        '''
        Download a ranking.

        Args:
            filename (str): The filename to save the ranking.
            month (str): The month of the ranking, e.g. 'Jan', 'Feb', etc.
            year (int): The year of the ranking.
            page (int): The page of the ranking.
        Raises:
            RankingDateError: If cannot download the ranking.
        Returns:
            str: The ranking in HTML format.
        '''
        endpoint = Utilities.ENDPOINT['soccerzz'][self.__category]
        url = Utilities.apply_query(endpoint, year, month, page)
        response = Utilities.request(url).decode('utf-8', 'ignore')
        try:
            return Utilities.save_file(filename, response)
        except RankingDateError as exc:
            raise exc

    def refresh(self) -> None:
        '''
        Refresh the cache.

        Raises:
            RankingDateError: If cannot delete the cache.
        '''
        try:
            Utilities.remove_files('.prf')
        except RankingDateError as exc:
            raise exc

    def get(self, **kwargs) -> [Team]:
        '''
        Get a FIFA ranking.

        Args:
            year (int): The year of the ranking.
            month (str): The month of the ranking, e.g. 'Jan', 'Feb', etc.
            page (int): The page of the ranking, each page contains 20 teams.
        Raises:
            RankingDateError: If the date is not available or the page is not valid.
        Returns:
            list: A list of Team objects.
        '''
        data = None
        month, year = self.__available_dates[0].split(' ')
        month, year = kwargs.get('month', month), kwargs.get('year', year)
        page = kwargs.get('page', 1)
        if not self.check_date(month, year):
            raise RankingDateError(f"Date {month} {year} is not available.")
        if not self.check_page(page):
            raise RankingError(f"Page {page} is not valid.")
        filename = f"{self.__category}_{month}-{year}-{page}.prf"
        exist = Utilities.file_exists(filename)
        data = Utilities.open_file(filename) if exist else self.__download(
            filename, month, year, page)
        parser = Parser(data, self.__category)
        parser.parse()
        date = month.title() + str(year)
        teams = [Team(date, *team_data) for team_data in parser.data]
        return teams
