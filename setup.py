from setuptools import setup
from pyrankingfifa import (
    __version__,
    __author__,
    __title__,
    __license__
)

with open('README.md') as file:
    long_description = file.read()

setup(
    name=__title__,
    version=__version__,
    author=__author__,
    license=__license__,
    description='Python library to get FIFA Ranking since 2007.',
    packages=['pyrankingfifa'],
    long_description_content_type="text/markdown",
    long_description=long_description,
    url='https://github.com/manucabral/pyrankingfifa',
    project_urls={
        'Bug Tracker': 'https://github.com/manucabral/pyrankingfifa/issues',
        'Documentation': 'https://github.com/manucabral/pyrankingfifa/readme.md',
    },
    python_requires=">=3.9",
    keywords=['fifa', 'ranking', 'soccer',
              'football', 'worldcup', 'fifaranking'],
    clasisfiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Football',
        'Topic :: Soccer',
        'Topic :: FIFA',
        'Topic :: FIFA Ranking',
        'Topic :: Software Development :: Libraries',
    ],
)
