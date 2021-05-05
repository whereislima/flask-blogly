from models import User, Post, PostTag, Tag, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
User.query.delete()
Post.query.delete()

# Add users
user1 = User(first_name="Li", last_name="Ma", image_url="https://bit.ly/3aIRDEd")



# Add posts
# post1 = Post(title="Digital Nomad", 
# content="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
# created_at=2021-04-26 19:43:03.221446, user_id=1)

db.session.add(user1)

db.session.commit()