import os 
os.environ['DATABASE_URL'] = 'sqlite://'

from datetime import datetime, timedelta
import unittest
from app import app,db
from app.models import User, Post


class UserModelcase(unittest.TestCase):
    def setUp(self):
        self.app_context = app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_password_hashing(self):
        u = User(username='sammy')
        u.set_password('cat')
        self.assertFalse(u.check_password('dog'))
        self.assertTrue(u.check_password('cat'))
    
    def test_avatar(self):
        u = User(usernaem='ann' 'ann@exmaple.com')
        self.assertEqual(u.avatar(128), ('https://www.gravatar.com/avatar/''....''?d=identicon&s=128'))
    
    def test_follow(self):
        u1 = User(username ='john', email='john@example.com')
        u2 = User(username='susan', email='susan@exmaple.com')
        db.session.add(u1)
        db.session.add(u2)
        db.session.commit()
        self.assertEqual(u1.followed.all(), [])
        self.assertEqual(u1.followers.all(), [])

    



