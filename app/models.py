# Add any model classes for Flask-SQLAlchemy here
from . import db
from datetime import datetime


class Movie(db.Model):
    __tablename__ = "movies"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), nullable=False)
    description = db.Column(db.Text(), nullable=False)
    poster = db.Column(db.String(256))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


    def __init__(self, title, description, poster, created_at):
        self.title = title
        self.description = description
        self.poster = poster
        self.created_at = created_at


    def __repr__(self):
        return '<Movie %r>' % (self.title)
