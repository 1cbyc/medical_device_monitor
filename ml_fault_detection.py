import pandas as pd
from sklearn.ensemble import IsolationForest

def train_model(df):
    model = IsolationForest()
    model.fit(df[['heart_rate', 'infusion_rate']])
    return model

def detect_faults(df, model):
    df['anomaly'] = model.predict(df[['heart_rate', 'infusion_rate']])
    faults = df[df['anomaly'] == -1]
    return faults

if __name__ == "__main__":
    df = pd.read_csv('data/real_time_data.csv')
    model = train_model(df)
    faults = detect_faults(df, model)
    print("Faults detected:", faults)
