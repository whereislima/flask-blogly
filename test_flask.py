from unittest import TestCase

from app import app
from models import db, User

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly_test'
app.config['SQLALCHEMY_ECHO'] = False

app.config['TESTING'] = True

app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

db.drop_all()
db.create_all()

class UserViewsTestCase(TestCase):
    """ Tests for views for Users. """

    def setUp(self):

        User.query.delete()

        user = User(first_name="Test1", last_name="Test1", image_url="https://bit.ly/3aCdDRa")
        db.session.add(user)
        db.session.commit()

        self.user_id = user.id
        self.user = user


    def tearDown(self):

        db.session.rollback()

    def test_list_users(self):
        with app.test_client() as client:
            resp = client.get("/users")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("Test1", html)

    def test_show_user(self):
        with app.test_client() as client:
            resp = client.get(f"/users/{self.user_id}")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("<h2>Test1 Test1</h2>", html)

    def test_add_user(self):
        with app.test_client() as client:
            data = {"first_name": "Test2", "last_name": "Test2", "image_url": "https://bit.ly/32Mmqf6"}
            resp = client.post("/users/new", data=data, follow_redirects=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("<h2>Test2 Test2</h2>", html)

    def test_edit_form(self):
        with app.test_client() as client:
            resp = client.get(f"/users/{self.user_id}")

            data = {"first_name": "Test2.1", "last_name": "Test2.1", "image_url": "https://bit.ly/3xmlMmv"}
            resp = client.post(f"/users/{self.user_id}", data=data, follow_redirects=True)

            self.assertEqual(resp.status_code, 200) 
            self.assertIn("<h2>Test2.1 Test2.1</h2>", html)
          
