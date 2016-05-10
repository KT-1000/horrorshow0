from imdbpie import Imdb


def get_horror_movies():
    imdb = Imdb()
    title = imdb.get_title_by_id("tt4062536")
    print title.title, title.credits

get_horror_movies()
