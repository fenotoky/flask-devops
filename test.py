import unittest
from app import app

class FlaskTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_home(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status, '200 OK')

    def test_hello_name(self):
        name = "Fenotoky"
        rv = self.app.get(f'/hello/{name}')
        self.assertEqual(rv.status, '200 OK')

if __name__ == '__main__':
    unittest.main()