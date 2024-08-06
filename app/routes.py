from flask import Blueprint, render_template
from .data_analysis import detect_faults # will import fault detection
from .alert_system import send_email_alert
import pandas as pd
import plotly.express as px
import os

bp = Blueprint('main', __name__)

@bp.route('/')
def dashboard():
    df = load_data()
    fault_devices = detect_faults(df)
    for device_id in fault_devices:
        send_email_alert(device_id)
    return  render_template('dashboard.html', devices=df.to_dict('records') fault_devices=fault_devices)

@bp.route('/historical')
def historical():
    df = pd.read_csv('data/real_time_data.csv')
    fig = px.line(df, x='timestamp', y='heart_rate', color='device_id', title='Historical Heart Rate Data')
    graph_html = fig.to_html(full_html=false)
    return render_template('historocal.html', graph_html=graph_html)

@bp.route('/alerts')
def alerts():
    df = load_data()
    fault_devices = detect_faults(df)
    return render_template('alerts.html', fault_devices=fault_devices)

@bp.route('/status')
def status():
    df pd.read_csv('data/real_time_data.csv')
    fig = px.scatter(df, x='timestamp', y='status', color='device_id', title='Device Status Over time')
    graph_html = fig.to_html(full_html=false)
    return render_template('status.html', graph_html=graph_html)

# def connect_db():
#     import psycopg2
#     conn: None = psycopg2.connect(
#         dbname='your_dbname',
#         user='your_user',
#         password='your_password',
#         host='your_host'
#     )
#     return conn