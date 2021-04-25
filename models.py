"""Models for Blogly."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)

DEFAULT_PROFILE_PIC = "https://bit.ly/3aCdDRa"


class User(db.Model): 

    __tablename__ = "users"

    id = db.Column(db.Integer, 
                    primary_key=True,
                    autoincrement=True)
    first_name = db.Column(db.Text,
                            nullable=False)
    last_name = db.Column(db.Text,
                            nullable=False)
    image_url = db.Column(db.Text, 
                            nullable=False,
                            default=DEFAULT_PROFILE_PIC)
