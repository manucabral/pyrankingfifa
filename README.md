## pyrankingfifa

A lightweight and zero dependencies Python library for extract the current FIFA World Ranking.

### Installation
PyPI package is not available yet, clone it.
```bash
git clone https://github.com/manucabral/pyrankingfifa.git
```

### Usage
Setting up
```py
from pyrankingfifa import Ranking

ranking = Ranking()
teams = ranking.teams()
```

Get first 20 teams of the ranking
```py
for team in teams:
    print(team.rank, team.name, team.points)
```

### Constributions
All constributions, bug reports or fixes and ideas are welcome.
