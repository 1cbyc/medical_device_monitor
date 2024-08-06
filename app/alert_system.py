import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email_alert(device_id):
    # sender_email = "your_email@example.com"
    # receiver_email = "provider_email@example.com"
    # password = "your_email_password"
    sender_email = os.getenv('SENDER_EMAIL')
    receiver_email = os.getenv('RECEIVER_EMAIL')
    password = os.getenv('EMAIL_PASSWORD')
    smtp_server = os.getenv('SMTP_SERVER')
    smtp_port = os.getenv('SMTP_PORT')

    message = MIMEMultipart("alternative")
    message["Subject"] = f"Alert: Fault detected in {device_id}"
    message["From"] = sender_email
    message["To"] = receiver_email

    text = f"A fault has been detected in device {device_id}. Immediate attention is required."
    part = MIMEText(text, "plain")

    message.attach(part)

    # with smtplib.SMTP_SSL("smtp.example.com", 465) as server:
    #     server.login(sender_email, password)
    #     server.sendmail(sender_email, receiver_email, message.as_string())
    #
    # print(f"Alert sent for data {device_id}")
    try:
        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        print(f"Alert sent for device {device_id}")
    except Exception as e:
        print(f"Failed to send alert for device {device_id}: {e}")

if __name__ == "__main__":
    send_email_alert("device_1")
