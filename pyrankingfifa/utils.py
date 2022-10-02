'''This module implements all utilities used in the library.'''

import os
import re
import json
import urllib.request
import random
from datetime import date

from pyrankingfifa.user_agents import USER_AGENTS
from pyrankingfifa.exceptions import RankingError


class Utilities:
    '''Utilities class core.'''

    ENDPOINT = {
        'soccerzz': {
            'mens': 'https://www.ceroacero.es/ranking_fifa.php',
            'womens': 'https://www.ceroacero.es/ranking_fifa_women.php'
        },
        'fifa': {
            'mens': 'https://www.fifa.com/fifa-world-ranking/men?dateId=id13750',
            'womens': 'https://www.fifa.com/fifa-world-ranking/women?dateId=ranking_20220805'
        }
    }

    MONTH = {
        'jan': 1,
        'feb': 2,
        'mar': 3,
        'apr': 4,
        'may': 5,
        'jun': 6,
        'jul': 7,
        'aug': 8,
        'sep': 9,
        'oct': 10,
        'nov': 11,
        'dec': 12
    }

    QUERY = '?ano_rank={}&mes_rank={}&pais=0&page={}'

    @ staticmethod
    def apply_query(url: str, year: int, month: str, page: int) -> str:
        '''
        Apply the query to an URL.

        Args:
            url (str): The url to apply the query.
            year (int): The year to apply the query.
            month (int): The month to apply the query.
            page (int): The page to apply the query.
        Returns:
            str: The url with the query applied.
        '''
        if isinstance(month, str):
            month = Utilities.MONTH[month.lower()]
        return url + Utilities.QUERY.format(year, month, page)

    @staticmethod
    def request(url: str) -> str:
        '''
        Request an URL.

        Args:
            url (str): The url to request.
        Raises:
            RankingError: If the request fails.
        Returns:
            str: The response of the request.
        '''
        headers = random.choice(USER_AGENTS)
        req = urllib.request.Request(url, headers=headers, method='GET')
        try:
            with urllib.request.urlopen(req) as response:
                return response.read()
        except urllib.error.HTTPError as exc:
            raise RankingError(f'Error requesting the ranking: {exc}') from exc

    @staticmethod
    def load_json(data: str) -> dict:
        '''
        Convert string data to json.

        Args:
            data (str): The string data to convert.
        Raises:
            RankingError: If cannot convert the data to json.
        Returns:
            dict: The data in json format.
        '''
        try:
            return json.loads(data)
        except json.JSONDecodeError as exc:
            raise RankingError(f'Error loading the ranking: {exc}') from exc

    @ staticmethod
    def findall(pattern: str, data: str, flags: int = 0) -> list:
        '''
        Find all matches in the data.

        Args:
            pattern (str): The pattern to search for.
            data (str): The data to search.
            flags (int): The flags to use.
        Raises:
            RankingError: If cannot find the pattern in the data.
        Returns:
            list: A list of matches.
        '''
        try:
            return re.findall(pattern, data, flags)
        except re.error as exc:
            raise RankingError(f'Error finding the ranking: {exc}') from exc

    @ staticmethod
    def file_exists(file: str) -> bool:
        '''
        Check if the file exists.

        Args:
            file (str): The file to check.
        Returns:
            bool: True if the file exists, False otherwise.
        '''
        try:
            with open(file, 'r') as f:
                return True
        except FileNotFoundError:
            return False

    @staticmethod
    def open_file(file: str) -> str:
        '''
        Open a file.

        Args:
            file (str): The file to open.
        Returns:
            str: The content of the file.
        '''
        try:
            with open(file, 'r') as file:
                return file.read()
        except FileNotFoundError as exc:
            raise RankingError(f'Error opening the file: {file}') from exc

    @staticmethod
    def save_file(file: str, data: str) -> object:
        '''
        Save data to a file.

        Args:
            file (str): The file to save the data.
            data (str): The data to save.
        Raises:
            RankingError: If cannot save the data to the file.
        Returns:
            object: The data saved to the file.
        '''
        try:
            with open(file, 'w', encoding='utf-8') as file:
                file.write(data)
                return data
        except FileNotFoundError as exc:
            raise RankingError(f'Error saving the file: {file}') from exc

    @staticmethod
    def remove_files(extension: str) -> None:
        '''
        Remove all files with the given extension.

        Args:
            extension (str): The extension to remove.
        '''
        for file in os.listdir():
            if file.endswith(extension):
                os.remove(file)
