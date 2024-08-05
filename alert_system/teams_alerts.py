import requests

def send_teams_alert(device_id, message):
    webhook_url = 'https://outlook.office.com/webhook/XXXXXXX'
    payload = {
        'text': f"Alert for device {device_id}: {message}"
    }
    requests.post(webhook_url, json=payload)

if __name__ == "__main__":
    send_teams_alert('device_1', 'Fault detected')
