from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Collection(db.Model):
    """ Collection is a group of Movies submitted by a User. """
    __tablename__ = "collection"

    collection_id = db.Column(db.Integer, primary_key=True)
    max_size = db.Column(db.Integer, default=10)
    name = db.Column(db.String(150))
    description = db.Column(db.String(10000))

    def __repr__(self):
        """ Provide more informative object info. """
        return "<%s: %s>" % (self.name, self.description)


class Association(db.Model):
    __tablename__ = "association"

    association_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    collection_id = db.Column(db.Integer, db.ForeignKey('collection.collection_id'))
    movie_id = db.Column(db.String, db.ForeignKey('movie.movie_id'))

    def __repr__(self):
        """ Provide more informative object info. """
        return "<association: %s collection: %s movie: %s>" % (self.association_id, self.collection_id, self.movie_id)


class Movie(db.Model):
    """ Movie record from IMDb. """
    __tablename__ = "movie"

    movie_id = db.Column(db.String(15), primary_key=True, index=True)
    title = db.Column(db.String(250))
    year = db.Column(db.Integer)
    rated = db.Column(db.String(10), nullable=True)
    release_date = db.Column(db.DateTime, nullable=True)
    runtime = db.Column(db.String(10), nullable=True)
    genre = db.Column(db.String(100))
    plot = db.Column(db.String(10000), nullable=True)
    language = db.Column(db.String(50), nullable=True)
    country = db.Column(db.String(50), nullable=True)
    poster_url = db.Column(db.String(500), nullable=True)
    imdb_url = db.Column(db.String(500))
    omdb_url = db.Column(db.String(500))

    def __repr__(self):
        """ Provide more informative object info. """
        return "<%d : %s>" % (self.movie_id, self.title)


class Showing(db.Model):
    """ A showing occurs in a theater for a movie. """
    __tablename__ = "showing"

    showing_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)
    movie_id = db.Column(db.String, db.ForeignKey('movie.movie_id'))
    theater_id = db.Column(db.Integer, db.ForeignKey('theater.theater_id'))

    def __repr__(self):
        """ Provide more informative object info. """
        return "<%s - %s>" % (self.start_time, self.end_time)


class Theater(db.Model):
    """ Theater information. """
    __tablename__ = "theater"

    theater_id = db.Column(db.Integer, autoincrement=True, primary_key=True, index=True)
    name = db.Column(db.String(150))
    location = db.Column(db.String(150))

    def __repr__(self):
        """ Provide more informative object info. """
        return "<theater: %d>" % self.name


# Helper functions
def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///horrorshow'
    db.app = app
    db.init_app(app)

if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.
    from horrorshow import app
    connect_to_db(app)
    print "Connected to DB."
