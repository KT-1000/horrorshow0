from bs4 import BeautifulSoup
from urllib import urlopen
# Populating a PostgreSQL database

# Scrape one local theater's site for horror showtimes
# Get movie information about that movie from IMDB using IMDbPY

# Look into format of rss/atom feed for horror blog

# Might be able to get location and theatre info from google maps API

# See if python meetup api is still viable
# get html document
html_doc = urlopen("http://www.imdb.com/search/title?genres=horror&sort=moviemeter,asc&title_type=feature")
# search for horror movies by popularity in html
# soup is one long string of html
soup = BeautifulSoup(html_doc, 'html.parser')
# get movie id and title from soup
# form URL according to id in following format: http://www.imdb.com/title/<movie_id>/
for result in soup.table:
    # print each out
    print result
