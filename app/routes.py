# from flask import render_template, redirect, url_for
from flask import render_template
import pandas as pd
from .data_analysis import detect_faults # will import fault detection
from .alert_system import send_email_alert
import plotly.express as px
import os
import psycopg2
# from app import create_app

# app = create_app()
# app = Flask(__name__)
#
# @app.route('/')
# def dashboard():
#     df = pd.read_csv('data/real_time_data.csv')
#     fig = px.line(df, x='timestamp', y='heart_rate', color='device_id', title='Heart Rate Over Time')
#     graph_html = fig.to_html(full_html=False)
#     return render_template('dashboard-v1.html', graph_html=graph_html)

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

    return render_template('dashboard-v1.html', devices=df.to_dict('records'), fault_devices=fault_devices)

@app.route('/historical')
def historical():
    df = pd.read_csv('data/real_time_data.csv')
    fig = px.line(df, x='timestamp', y='heart_rate', color='device_id', title='Historical Heart Rate Data')
    graph_html = fig.to_html(full_html=False)
    return render_template('historical.html', graph_html=graph_html)
# @app.route('/')
# def dashboard():
#     df = pd.read_csv('data/simulated_data.csv')
#     fault_devices = df[df['status'] == 'FAULT']['device_id'].unique()
#     return render_template('dashboard-v1.html', devices=df.to_dict('records'), fault_devices=fault_devices)

@app.route('/alerts')
def alerts():
    if os.path.exists('data/simulated_data.csv'):
        df = pd.read_csv('data/simulated_data.csv')
    else:
        df = pd.DataFrame(columns=["device_id", "timestamp", "status", "heart_rate", "infusion_rate"])

    fault_devices = df[df['status'] == 'FAULT']['device_id'].unique()
    return render_template('alerts.html', fault_devices=fault_devices)

@app.route('/status')
def status():
    df = pd.read_csv('data/real_time_data.csv')
    fig = px.scatter(df, x='timestamp', y='status', color='device_id', title='Device Status Over Time')
    graph_html = fig.to_html(full_html=False)
    return render_template('status.html', graph_html=graph_html)

def connect_db():
    conn: None = psycopg2.connect(
        dbname='your_dbname',
        user='your_user',
        password='your_password',
        host='your_host'
    )
    return conn