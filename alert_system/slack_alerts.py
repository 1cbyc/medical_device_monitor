import requests

def send_slack_alert(device_id, message):
    webhook_url = 'https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX'
    payload = {
        'text': f"Alert for device {device_id}: {message}"
    }
    requests.post(webhook_url, json=payload)

if __name__ == "__main__":
    send_slack_alert('device_1', 'Fault detected')
