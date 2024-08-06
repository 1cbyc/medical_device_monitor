import os
import psycopg2
from flask import Blueprint, render_template
from .data_analysis import detect_faults, load_data # will import fault detection
from .alert_system import send_email_alert
import pandas as pd
import plotly.express as px
from dotenv import  load_dotenv

load_data() # to load the env var for db from .env

bp = Blueprint('main', __name__)

def connect_db():
    conn = psycopg2.connect(
        dbname=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_HOST')
    )
    return conn

@bp.route('/')
def dashboard():
    df = load_data()
    fault_devices = detect_faults(df)
    for device_id in fault_devices:
        send_email_alert(device_id)
    return  render_template('dashboard.html', devices=df.to_dict('records'), fault_devices=fault_devices)

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
    df = pd.read_csv('data/real_time_data.csv')
    fig = px.scatter(df, x='timestamp', y='status', color='device_id', title='Device Status Over time')
    graph_html = fig.to_html(full_html=false)
    return render_template('status.html', graph_html=graph_html)

def load_data():
    # let's assume this function loads data from the db or the csv
    conn = connect_db()
    query = "SELECT * FROM your_table"
    df = pd.read_sql(query, conn)
    conn.close()
    return df