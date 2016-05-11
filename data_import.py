from imdbpie import Imdb
from bs4 import BeautifulSoup
import urllib2


def get_horror_movies():
    imdb = Imdb()
    title = imdb.get_title_by_id("tt4062536")
    print title.title


def scrape_imdb(movie_file):
    ''' Get movie information from IMDb to seed horrorshow database. '''
    # Get html from URL
    html = urllib2.urlopen("http://www.imdb.com/search/title?genres=horror&sort=moviemeter,asc&title_type=feature")
    soup = BeautifulSoup(html, 'html.parser')

    with open(movie_file, 'w') as cur_file:
        for link in soup.find_all('a', href=True):
            # get only links containing imdb id of result movies
            if '/title/tt' in link['href'] and 'vote' not in link['href']:
                # put only movie ID in text file
                imdb_id = (link['href'].split('/'))[2]
                cur_file.write(imdb_id + '\n')

scrape_imdb("movies.txt")
