import unittest
from app import app
from app.data_processing import generate_simulated_data


class TestWebIntegration(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        # Generate data for testing
        generate_simulated_data()

    def test_dashboard_integration(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Device Dashboard', response.data)

    def test_alerts_integration(self):
        response = self.app.get('/alerts')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Alerts', response.data)


if __name__ == "__main__":
    unittest.main()
