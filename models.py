from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Movie(db.Model):
    """ Movie record from IMDb. """
    imdb_id = db.Column(db.Integer, primary_key=True, index=True)
    title = db.Column(db.String(256))
    image_url = db.Column(db.String(256), nullable=True)
    rating = db.Column(db.String(8), nullable=True)
    runtime = db.Column(db.Integer, nullable=True)
    description = db.Column(db.String(5000), nullable=True)


class Showing(db.Model):
    """ A showing occurs in a theater for a movie. """
    showing_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    time = db.Column(db.DateTime)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.imdb_id'))
    theater_id = db.Column(db.Integer, db.ForeignKey('theater.theater_id'))


class Theater(db.Model):
    """ Theater information from Google Movies Showtimes. """
    theater_id = db.Column(db.Integer, primary_key=True, index=True)
    location = db.Column(db.String(128))


# Helper functions
def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PstgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///horrorshow'
    db.app = app
    db.init_app(app)

if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app
    connect_to_db(app)
    print "Connected to DB."
