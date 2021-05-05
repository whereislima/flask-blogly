"""Models for Blogly."""

from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

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
    posts = db.relationship('Post')

    @property 
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

class Post(db.Model):

    __tablename__ = "posts"

    id = db.Column(db.Integer, 
                    primary_key=True,
                    autoincrement=True)

    title = db.Column(db.Text, 
                        nullable=False)
    content = db.Column(db.Text, 
                        nullable=False)
    created_at = db.Column(db.DateTime, 
                            nullable=False,
                            default=datetime.datetime.now)

    user_id = db.Column(db.Integer,
                            db.ForeignKey('users.id'),
                            nullable=False)
    user = db.relationship('User')

    post_tag = db.relationship('PostTag')

    
   
class PostTag(db.Model):

    __tablename__ = "posts_tags"

    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), primary_key=True)
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'), primary_key=True)

    

class Tag(db.Model):

    __tablename__ = "tags"

    id = db.Column(db.Integer, 
                    primary_key=True, 
                    autoincrement=True)
    name = db.Column(db.Text, 
                        nullable=False, 
                        unique=True)
    posts = db.relationship('Post', secondary='posts_tags', backref='tags')

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)