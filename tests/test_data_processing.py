import unittest
import pandas as pd
from app.data_processing import load_data, preprocess_data


class TestDataProcessing(unittest.TestCase):

    def setUp(self):
        # this will create a sample CSV file for testing
        data = {
            'device_id': ['device_1', 'device_2', 'device_1'],
            'timestamp': ['2024-08-05 12:00:00', '2024-08-05 12:01:00', '2024-08-05 12:02:00'],
            'status': ['OK', 'FAULT', 'FAULT'],
            'heart_rate': [75, 80, 78],
            'infusion_rate': [1.5, 2.0, 1.8]
        }
        df = pd.DataFrame(data)
        df.to_csv('data/test_data.csv', index=False)

    def test_load_data(self):
        df = load_data('data/test_data.csv')
        self.assertEqual(df.shape[0], 3)

    def test_preprocess_data(self):
        df = load_data('data/test_data.csv')
        processed_df = preprocess_data(df)
        self.assertIn('heart_rate_normalized', processed_df.columns)

    def tearDown(self):
        os.remove('data/test_data.csv')


if __name__ == "__main__":
    unittest.main()
