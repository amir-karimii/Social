import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from ssl import create_default_context

# Environment variables
MAIL_HOST = os.getenv("MAIL_HOST", "smtp.c1.liara.email")
MAIL_PORT = int(os.getenv("MAIL_PORT", 465))
MAIL_USER = os.getenv("MAIL_USER", 'amazing_chaum_danl8q')
MAIL_PASSWORD = os.getenv("MAIL_PASSWORD", 'c08f7aa8-f96d-4ad4-8948-02d38034a5c8')
MAIL_FROM_ADDRESS = os.getenv("MAIL_FROM_ADDRESS", 'info@amirkarimiweb.ir')
MAIL_FROM_NAME = os.getenv("MAIL_FROM_NAME", 'chasto-plus')

def send_email(to_address, subject, body):
    try:
        # Enforce TLS
        context = create_default_context()

        # Connect to the server
        with smtplib.SMTP_SSL(MAIL_HOST, MAIL_PORT, context=context) as server:
            server.login(MAIL_USER, MAIL_PASSWORD)

            # Prepare the email
            msg = MIMEMultipart()
            msg['From'] = f"{MAIL_FROM_NAME} <{MAIL_FROM_ADDRESS}>"
            msg['To'] = to_address
            msg['Subject'] = subject
            msg.add_header('x-liara-tag', 'test-tag')  # Add custom header
            msg.attach(MIMEText(body, 'plain'))

            # Send the email
            server.sendmail(MAIL_FROM_ADDRESS, to_address, msg.as_string())
            print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Example usage
if __name__ == "__main__":
    recipient = "mohsensalare@gmail.com"
    subject = "Test Email"
    body = "marg ba chaheston amrica."
    send_email(recipient, subject, body)
