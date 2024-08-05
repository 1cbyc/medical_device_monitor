import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email_alert(device_id):
    sender_email = "your_email@example.com"
    receiver_email = "provider_email@example.com"
    password = "your_email_password"

    message = MIMEMultipart("alternative")
    message["Subject"] = f"Alert: Fault detected in {device_id}"
    message["From"] = sender_email
    message["To"] = receiver_email

    text = f"A fault has been detected in device {device_id}. Immediate attention is required."
    part = MIMEText(text, "plain")

    message.attach(part)

    with smtplib.SMTP_SSL("smtp.example.com", 465) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

if __name__ == "__main__":
    send_email_alert("device_1")
