import champion_gg

stats = {"champion.gg": champion_gg.stats,
         "u.gg": None}

print(stats)

import urllib.request
import bs4
from collections import OrderedDict

# Get Raw HTML-File
req = urllib.request.Request("https://www.leagueofgraphs.com/champions/builds", headers={'User-Agent': 'Mozilla/5.0'})
page = urllib.request.urlopen(req).read()

# Parse Html
soup = bs4.BeautifulSoup(page, "html5lib")

# Navigate to Champion-Winrate-Data
data: str = soup.body.find("table", attrs={"class": "data_table"})

print(data)
