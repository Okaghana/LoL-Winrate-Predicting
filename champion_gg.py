import urllib.request
import bs4
from collections import OrderedDict

# Get Raw HTML-File
req = urllib.request.Request("https://champion.gg/statistics/", headers={'User-Agent': 'Mozilla/5.0'})
page = urllib.request.urlopen(req).read()

# Parse Html
soup = bs4.BeautifulSoup(page, "html5lib")

# Navigate to Champion-Winrate-Data
data: str = soup.body.find(attrs={'class': ['primary-hue']}).find(attrs={'class': ['main-container']}).find(attrs={'class': ['page-content']}) \
    .find_all(name="script", recursive=False)[1].string[23:-2]

# Parse and Evaluate String
data = data.replace("null", "None")
data = eval(data)

# Loop trough every Champion
stats = {}
for champion in data:
    name = champion["key"]
    winRatio = champion["general"]["winPercent"]

    # Add ChampionEntry
    if name not in stats:
        stats[name] = winRatio

    # Append to List
    else:
        if type(stats[name]) is not list:
            stats[name] = [stats[name]]
        stats[name].append(winRatio)

# Calculate average if necessary
for i in range(len(stats)):
    name = list(stats.keys())[i]

    if type(stats[name]) is list:
        total = sum(stats[name])
        stats[name] = total/len(stats[name])

# Decimal Precision
for i in stats:
    stats[i] = round(stats[i], 3)

# Sort
stats = dict(OrderedDict(sorted(stats.items())))