"""Blogly application."""

from flask import Flask, request, redirect, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User, Post

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "avocado"
app.config['SQLALCHEMY_ECHO'] = True

# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)
db.create_all()

# USER ROUTES
@app.route("/")
def redirect_users_list():

    return redirect("/users")

@app.route("/users")
def show_users_list():

    users = User.query.all()

    return render_template("/users/listing.html", users=users)


@app.route("/users/new")
def show_add_users_form():

    return render_template("/users/form.html")

@app.route("/users/new", methods=["POST"])
def add_user():

    first_name = request.form["first-name"]
    last_name = request.form["last-name"]
    image_url = request.form["image-url"] or None

    new_user = User(first_name=first_name, last_name=last_name, image_url=image_url)
    db.session.add(new_user)
    db.session.commit()

    return redirect("/users")

@app.route("/users/<int:user_id>")
def show_user_detail(user_id):

    user = User.query.get_or_404(user_id)
   
    return render_template("/users/detail.html", user=user)

@app.route("/users/<int:user_id>/edit")
def show_edit_form(user_id):

    user = User.query.get_or_404(user_id)
    return render_template("/users/edit.html", user=user)

@app.route("/users/<int:user_id>/edit", methods=["POST"])
def edit_user(user_id):

    user = User.query.get_or_404(user_id)

    user.first_name = request.form["new-first-name"]
    user.last_name = request.form["new-last-name"]
    user.image_url = request.form["new-image-url"] or None

    return redirect("/users")

@app.route("/users/<int:user_id>/delete", methods=["POST"])
def delete_user(user_id):

    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()

    return redirect("/users")

# POST ROUTES ----------------------------------------------

@app.route("/users/<int:user_id>/posts/new")
def show_post_form(user_id):

    user = User.query.get_or_404(user_id)
    return render_template("/users/posts/form.html", user=user)

@app.route("/users/<int:user_id>/posts/new", methods=["POST"])
def add_post(user_id):

    user = User.query.get_or_404(user_id)
    title = request.form["title"]
    content = request.form["content"]

    post = Post(title=title, content=content, user=user)
    
    db.session.add(post)
    db.session.commit()

    return redirect(f"/users/{user_id}")

@app.route("/posts/<int:post_id>")
def post_detail(post_id):

    post = Post.query.get_or_404(post_id)

    return render_template("/users/posts/detail.html", post=post)

@app.route("/posts/<int:post_id>/edit")
def show_post_edit_form(post_id):

    post = Post.query.get_or_404(post_id)

    return render_template("/users/posts/edit.html", post=post)

@app.route("/posts/<int:post_id>/edit", methods=["POST"])
def edit_post(post_id):

    post = Post.query.get_or_404(post_id)

    post.title = request.form["title"]
    post.content = request.form["content"]

    db.session.add(post)
    db.session.commit()

    return redirect(f"/users/{post.user_id}")

@app.route("/posts/<int:post_id>/delete", methods=["POST"])
def delete_post(post_id):

    post = Post.query.get_or_404(post_id)

    db.session.delete(post)
    db.session.commit()

    return redirect(f"/users/{post.user_id}")
