from flask import render_template, redirect, url_for
import pandas as pd
from .alert_system import send_email_alert
import os
# from app import create_app

# app = create_app()

@app.route('/')
def dashboard():
    # will load the data
    if os.path.exists('data/simulated_data.csv'):
        df = pd.read_csv('data/simulated_data.csv')
    else:
        df = pd.DataFrame(columns=["device_id", "timestamp", "status"])

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
