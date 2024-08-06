import pandas as pd

def 
def load_data():
    df = pd.read_csv('data/simulated_data.csv')
    return df

def detect_faults(df):
    fault_devices = df[df['status'] == 'FAULT']['device_id'].unique()
    return fault_devices

if __name__ == "__main__":
    df = load_data()
    fault_devices = detect_faults(df)
    print("Faulty devices:", fault_devices)
