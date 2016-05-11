from imdbpie import Imdb
from bs4 import BeautifulSoup
import urllib2


def parse_imdb(movie_file):
    ''' Get movie information from IMDb to seed horrorshow database.
        Create list of IMDb URLs representing the results for horror genre search
        on IMDb.
        For each URL in the list, open that URL
        Make it into soup
        From each link containing the search result's imdb_id, get the imdb_id
        and write it to the movies.txt file.
    '''
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


def get_horror_movies(imdb_id):
    """ For each imdb_id in the movies.txt file, get the movie info using imdbpie
        Write to movie_entry.txt file, which will be read to populate db.
    """
    imdb = Imdb()
    title = imdb.get_title_by_id(imdb_id)
    print title.title

parse_imdb("movies.txt")
