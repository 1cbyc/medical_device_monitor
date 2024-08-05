# import os
import unittest
import pandas as pd
from app.fault_detection import detect_faults

class TestFaultDetection(unittest.TestCase):

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

    def test_detect_faults(self):
        df = pd.read_csv('data/test_data.csv')
        faults = detect_faults(df)
        self.assertIn('device_2', faults)
        self.assertIn('device_1', faults)

    def tearDown(self):
        os.remove('data/test_data.csv')

if __name__ == "__main__":
    unittest.main()
