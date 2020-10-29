import requests
from bs4 import BeautifulSoup

class movie:
    def __init__(self, name, year, rating):
        self.name = name
        self.year = year
        self.rating = rating



movieObjectList = []
r = requests.get("https://www.imdb.com/chart/top/")
soup = BeautifulSoup(r.content, 'html.parser')
movienames = soup.find_all('td', attrs={"class":"titleColumn"})

for content in movienames:
    string_title = content.a.text
    rate = content.parent.find('td', attrs = {"class":"ratingColumn imdbRating"})
    string_year = content.parent.find('span', attrs = {"class":"secondaryInfo"}).text.split("(")[1].split(")")[0]
    string_rate = rate.strong.text
    newMovie = movie(string_title,string_year,string_rate);
    movieObjectList.append(newMovie)

"""dict structre: key is the rating, value is the how many times found"""

ratingDict = {}
#d[key] = d.get(key, 0) + 1
for mov in movieObjectList:
    if mov.rating not in ratingDict:
        ratingDict[mov.rating] = 1
    else:
        ratingDict[mov.rating] = ratingDict.get(mov.rating) + 1


for val in ratingDict:
    print(val,":",ratingDict.get(val))


def newfunc():
	print("furkan1 added a new function")

