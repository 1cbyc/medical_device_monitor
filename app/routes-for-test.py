def load_data():
    # Temporarily return an empty DataFrame for testing purposes
    return pd.DataFrame()

@bp.route('/')
def dashboard():
    df = load_data()
    fault_devices = detect_faults(df)
    for device_id in fault_devices:
        send_email_alert(device_id)
    return render_template('dashboard.html', devices=df.to_dict('records'), fault_devices=fault_devices)

@bp.route('/historical')
def historical():
    # Temporarily use a sample DataFrame
    df = pd.DataFrame({
        'timestamp': ['2024-01-01', '2024-01-02'],
        'heart_rate': [70, 75],
        'device_id': [1, 1]
    })
    fig = px.line(df, x='timestamp', y='heart_rate', color='device_id', title='Historical Heart Rate Data')
    graph_html = fig.to_html(full_html=False)
    return render_template('historical.html', graph_html=graph_html)

@bp.route('/alerts')
def alerts():
    df = load_data()
    fault_devices = detect_faults(df)
    return render_template('alerts.html', fault_devices=fault_devices)

@bp.route('/status')
def status():
    # Temporarily use a sample DataFrame
    df = pd.DataFrame({
        'timestamp': ['2024-01-01', '2024-01-02'],
        'status': ['active', 'inactive'],
        'device_id': [1, 1]
    })
    fig = px.scatter(df, x='timestamp', y='status', color='device_id', title='Device Status Over time')
    graph_html = fig.to_html(full_html=False)
    return render_template('status.html', graph_html=graph_html)
