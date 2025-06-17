from app import create_app, db
import unittest
from config import TestConfig


class AuthTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.app.config['TESTING'] = True
        self.app.config['WTF_CSRF_ENABLED'] = False
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def register_user(self):
        return self.client.post('/register', data={
            'username': 'testuser',
            'email': 'test@example.com',
            'password': '123456',
            'confirm_password': '123456'
        }, follow_redirects=True)

    def test_register(self):
        response = self.register_user()
        self.assertEqual(response.status_code, 200)
        self.assertIn('Account created', response.get_data(as_text=True))

    def test_login(self):
        self.register_user()
        response = self.client.post('/login', data={
            'email': 'test@example.com',
            'password': '123456'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn('<h1>Пости</h1>', response.get_data(as_text=True))
