from flask import Flask, render_template, redirect, request, flash, session
from models import connect_to_db, Movie

app = Flask(__name__)
# Required to use Flask sessions and the debug toolbar
app.secret_key = "ChaosReigns"
app.config['DEBUG'] = True
# set up SQLAlchemy with app as context
connect_to_db(app)


@app.route('/')
def index():
    """ Show the main page, with featured collection(s) and any horror movies currently in theater. """
    # get the "featured" collection to display at top of page

    # get movies now playing to display in second row
    movies = Movie.query.all()

    return render_template("index.html", movies=movies)

if __name__ == '__main__':
    app.run()
