## pyrankingfifa

A lightweight and zero dependencies Python library that allows you to extract the Ranking FIFA since 2007.

This library wraps the FIFA Ranking through ceroaceros/soccerzz website.
Note this isn't affiliated with FIFA or ceroaceros.

### Installation
From PyPI
```bash
pip install pyrankingfifa
```
From source code clone it
```bash
git clone https://github.com/manucabral/pyrankingfifa.git
```

### Usage
Setting up
```py
from pyrankingfifa import Ranking

mens_ranking = Ranking('mens')
```
> womens ranking is not available for now

Let's get current ranking.
```py
ranking = mens_ranking.get()
for team in ranking:
    print(team.rank, team.name, team.points)
```
> If you need more rank positions apply the param page=id

Let's get a specific ranking date.
```py
ranking = mens.get(year=2018, month='aug')
for team in teams:
    print(team)
```
> The library saves all requests rankings for a faster request speed, if you want to remove these files call refresh() method.

### Constributions
All constributions, bug reports or fixes and ideas are welcome.
