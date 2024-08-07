# Setting up the SMTP to use

You can use an SMTP server like Gmail, SendGrid, or any other email service provider.

**1. Using Gmail SMTP**

* Ensure you have a Gmail account.
* Enable "Less secure app access" for your Gmail account in your account settings.
* Update your .env file with the following details:

```plaintext
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=your_gmail_username
SMTP_PASSWORD=your_gmail_password
```
**2. Using SendGrid**

* Sign up for a SendGrid account.
* Create an API key.
* Update your .env file with the following details:

```plaintext
SMTP_SERVER=smtp.sendgrid.net
SMTP_PORT=587
SMTP_USERNAME=apikey
SMTP_PASSWORD=your_sendgrid_api_key
```