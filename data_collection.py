import pandas as pd
import numpy as np
import time

def generate_simulated_data():
    device_ids = [f"device_{i}" for i in range(1, 11)]
    data = []

    for _ in range(100):
        for device_id in device_ids:
            status = np.random.choice(["OK", "FAULT"])
            data.append({
                "device_id": device_id,
                "timestamp": pd.Timestamp.now(),
                "status": status,
                "heart_rate": np.random.randint(60, 100),
                "infusion_rate": np.random.uniform(0.5, 5.0)
            })
            time.sleep(0.1)

    df = pd.DataFrame(data)
    df.to_csv('data/simulated_data.csv', index=False)

if __name__ == "__main__":
    generate_simulated_data()
