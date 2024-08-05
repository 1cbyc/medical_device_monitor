from flask import render_template
from app import create_app
import pandas as pd

app = create_app()

@app.route('/')
def dashboard():
    df = pd.read_csv('data/simulated_data.csv')
    fault_devices = df[df['status'] == 'FAULT']['device_id'].unique()
    return render_template('dashboard.html', devices=df.to_dict('records'), fault_devices=fault_devices)

@app.route('/alerts')
def alerts():
    df = pd.read_csv('data/simulated_data.csv')
    fault_devices = df[df['status'] == 'FAULT']['device_id'].unique()
    return render_template('alerts.html', fault_devices=fault_devices)
