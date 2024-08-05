import unittest
from app import app


class TestWebInterface(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_dashboard(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Device Dashboard', response.data)

    def test_alerts(self):
        response = self.app.get('/alerts')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Alerts', response.data)


if __name__ == "__main__":
    unittest.main()
