from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Movie(db.Model):
    """ Movie record from IMDb. """
    imdb_id = db.Column(db.Integer, primary_key=True, index=True)
    title = db.Column(db.String(256))
    


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
