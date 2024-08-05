import requests
import pandas as pd

def fetch_device_data(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error fetching data: {response.status_code}")

def save_data(data):
    df = pd.DataFrame(data)
    df.to_csv('data/real_time_data.csv', index=False)

if __name__ == "__main__":
    api_url = 'https://api.medicaldevice.com/data'  # Replace with actual API URL
    data = fetch_device_data(api_url)
    save_data(data)
