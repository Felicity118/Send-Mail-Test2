import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email():
    # Email configuration
    sender_email = "michele.usher@krilldesign.net"
    receiver_email = "michele.usher@studbocconi.it"
    password = "Krill2018!"
    smtp_server = "it38.siteground.eu"
    smtp_port = 587

    # Create a message object
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = "Test Email"

    # Email body
    body = "This is a test email sent using Python."
    message.attach(MIMEText(body, 'plain'))

    # Connect to the SMTP server
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Secure the connection
    server.login(sender_email, password)

    # Send the email
    server.sendmail(sender_email, receiver_email, message.as_string())

    # Close the connection
    server.quit()


