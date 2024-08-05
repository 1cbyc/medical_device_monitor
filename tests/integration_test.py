import unittest
from app.data_processing import load_data
from app.fault_detection import detect_faults


class TestIntegration(unittest.TestCase):

    def setUp(self):
        data = {
            'device_id': ['device_1', 'device_2', 'device_1'],
            'timestamp': ['2024-08-05 12:00:00', '2024-08-05 12:01:00', '2024-08-05 12:02:00'],
            'status': ['OK', 'FAULT', 'FAULT'],
            'heart_rate': [75, 80, 78],
            'infusion_rate': [1.5, 2.0, 1.8]
        }
        df = pd.DataFrame(data)
        df.to_csv('data/test_data.csv', index=False)

    def test_data_flow(self):
        df = load_data('data/test_data.csv')
        faults = detect_faults(df)
        self.assertGreater(len(faults), 0)

    def tearDown(self):
        os.remove('data/test_data.csv')


if __name__ == "__main__":
    unittest.main()
