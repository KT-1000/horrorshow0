from imdbpie import Imdb
from bs4 import BeautifulSoup
import urllib2


def get_movie_ids(id_file):
    ''' Get movie information from IMDb to seed horrorshow database.
        Create list of IMDb URLs representing the results for horror genre search
        on IMDb.
        For each URL in the list, open that URL
        Make it into soup
        From each link containing the search result's imdb_id, get the imdb_id
        and write it to the movies.txt file.
        Return list of IMDb IDs.
    '''
    # list of imdb id numbers to pass to use in
    imdb_ids = []

    # Get html from URL, format 'http://www.imdb.com/search/title?genres=horror&sort=moviemeter,asc&start=51&title_type=feature'
    html = urllib2.urlopen("http://www.imdb.com/search/title?genres=horror&sort=moviemeter,asc&title_type=feature")
    soup = BeautifulSoup(html, 'html.parser')

    with open("movie_ids.txt", 'w') as cur_file:
        for link in soup.find_all('a', href=True):
            # get only links containing imdb id of result movies
            if '/title/tt' in link['href'] and 'vote' not in link['href']:
                # only need movie id
                imdb_id = (link['href'].split('/'))[2]
                # append imdb id number to imdb_ids list, which will be returned
                imdb_ids.append(imdb_id)
                # write imdb id to file so we can read the file as an alternative to scraping IMDb directly in the future.
                cur_file.write(imdb_id + '\n')
    return imdb_ids


def get_movie_info(imdb_ids, out_file):
    """ For each imdb_id in the movies.txt file, get the movie info using imdbpie
        Write to movie_entry.txt file, which will be read to populate db.
    """
    # connect to IMDb using imdbpie
    imdb = Imdb()
    with open(out_file, 'w') as movies_file:
        for imdb_id in imdb_ids:
            title_obj = imdb.get_title_by_id(imdb_id)
            title = title_obj.title
            line = imdb_id + '|' + title + '\n'
            movies_file.write(line)
