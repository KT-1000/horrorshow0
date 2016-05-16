from flask import Flask, render_template, redirect, request, flash, session
from models import Movie, Collection, Association, Showing, Theater
from jinja2 import StrictUndefined

app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ChaosReigns"


@app.route('/')
def index():
    """ Show the main page, with featured collection(s) and any horror movies currently in theater. """
    # get the "featured" collection to display at top of page

    # get movies now playing to display in second row
    movies = Movie.query.all()

    return render_template("index.html", movies=movies)

if __name__ == '__main__':
    app.run()
