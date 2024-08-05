from twilio.rest import Client

def send_sms_alert(device_id, message):
    account_sid = 'your_account_sid'
    auth_token = 'your_auth_token'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=f"Alert for device {device_id}: {message}",
        from_='+1234567890',  # Your Twilio number
        to='+0987654321'  # Recipient number
    )

if __name__ == "__main__":
    send_sms_alert('device_1', 'Fault detected')
