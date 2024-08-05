# from flask import render_template, redirect, url_for
from flask import render_template
import pandas as pd
from .data_analysis import detect_faults # will import fault detection
from .alert_system import send_email_alert
import plotly.express as px
import os
# from app import create_app

# app = create_app()
app = Flask(__name__)

@app.route('/')
def dashboard():
    # will load the data
    if os.path.exists('data/simulated_data.csv'):
        df = pd.read_csv('data/simulated_data.csv')
    else:
        df = pd.DataFrame(columns=["device_id", "timestamp", "status", "heart_rate", "infusion_rate"])

    # detect faults
    fault_devices = df[df['status'] == 'FAULT']['device_id'].unique()

    # send alerts
    for device_id in fault_devices:
        send_email_alert(device_id)

    return render_template('dashboard.html', devices=df.to_dict('records'), fault_devices=fault_devices)

# @app.route('/')
# def dashboard():
#     df = pd.read_csv('data/simulated_data.csv')
#     fault_devices = df[df['status'] == 'FAULT']['device_id'].unique()
#     return render_template('dashboard.html', devices=df.to_dict('records'), fault_devices=fault_devices)

@app.route('/alerts')
def alerts():
    if os.path.exists('data/simulated_data.csv'):
        df = pd.read_csv('data/simulated_data.csv')
    else:
        df = pd.DataFrame(columns=["device_id", "timestamp", "status", "heart_rate", "infusion_rate"])

    fault_devices = df[df['status'] == 'FAULT']['device_id'].unique()
    return render_template('alerts.html', fault_devices=fault_devices)
