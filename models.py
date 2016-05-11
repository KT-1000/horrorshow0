from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Movie(db.Model):
    """ Movie record from IMDb. """
    __tablename__ = "movie"

    imdb_id = db.Column(db.Integer, primary_key=True, index=True)
    title = db.Column(db.String(250))
    rating = db.Column(db.String(10), nullable=True)
    release_date = db.Column(db.DateTime, nullable=True)
    runtime = db.Column(db.Integer, nullable=True)
    genre = db.Column(db.String(250))
    plot = db.Column(db.String(20000), nullable=True)
    language = db.Column(db.String(50), nullable=True)
    poster_url = db.Column(db.String(500), nullable=True)
    detail_url = db.Column(db.String(250))

    def __repr__(self):
        """ Provide more informative object info. """
        return "<imdb_id: %d title: %s>" % (self.imdb_id, self.title)


class Showing(db.Model):
    """ A showing occurs in a theater for a movie. """
    __tablename__ = "showing"

    showing_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    time = db.Column(db.DateTime)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.imdb_id'))
    theater_id = db.Column(db.Integer, db.ForeignKey('theater.theater_id'))

    def __repr__(self):
        """ Provide more informative object info. """
        return "<time: %s>" % (self.time)


class Theater(db.Model):
    """ Theater information. """
    __tablename__ = "theater"

    theater_id = db.Column(db.Integer, primary_key=True, index=True)
    name = db.Column(db.String(150))
    location = db.Column(db.String(250))

    def __repr__(self):
        """ Provide more informative object info. """
        return "<theater: %d>" % (self.name)


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
