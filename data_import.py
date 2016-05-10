from imdbpie import Imdb
from bs4 import BeautifulSoup
import urllib2


def get_horror_movies():
    imdb = Imdb()
    title = imdb.get_title_by_id("tt4062536")
    print title.title


def scrape_imdb():
    ''' Get movie information from IMDb to seed horrorshow database. '''
    html = urllib2.urlopen("http://www.imdb.com/search/title?genres=horror&sort=moviemeter,asc&title_type=feature")
    soup = BeautifulSoup(html, 'html.parser')

    for film_link in soup.find_all('a', href=True):
        if '/title/tt' in film_link['href'] and 'vote' not in film_link['href']:
            print film_link['href']

scrape_imdb()
