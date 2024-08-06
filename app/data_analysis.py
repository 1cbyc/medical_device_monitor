import pandas as pd
import os

def load_data():
    if os.path.exists('data/simulated_data.csv'):
        df = pd.read_csv('data/simulated_data.csv')
    else:
        df = pd.DataFrame(columns=["device_id", "timestamp", "status", "heart_rate", "infusion_rate"])
    return df
# def load_data():
#     df = pd.read_csv('data/simulated_data.csv')
#     return df

def detect_faults(df):
    fault_devices = df[df['status'] == 'FAULT']['device_id'].unique()
    return fault_devices

# if __name__ == "__main__":
#     df = load_data()
#     fault_devices = detect_faults(df)
#     print("Faulty devices:", fault_devices)
