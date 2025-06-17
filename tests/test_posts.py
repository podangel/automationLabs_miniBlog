from app import create_app, db
import unittest
from config import TestConfig


class PostTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app.config['TESTING'] = True
        self.app.config['WTF_CSRF_ENABLED'] = False
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()

        self.client.post('/register', data={
            'username': 'user',
            'email': 'u@example.com',
            'password': '123456',
            'confirm_password': '123456'
        }, follow_redirects=True)

        self.client.post('/login', data={
            'email': 'u@example.com',
            'password': '123456'
        }, follow_redirects=True)

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_create_post(self):
        response = self.client.post('/create_post', data={
            'title': 'Test Post',
            'content': 'This is a test post.'
        }, follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn('Post created', response.get_data(as_text=True))
