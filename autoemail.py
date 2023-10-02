import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
sender_email = "your@gmail.com"  # Your Gmail email address
subject = "Test Email"
message = "This is a test email sent from Python."

# App Password (Generated in Gmail Account Settings)
app_password = "your_app_password"

# Read recipient email addresses from a text file
with open("recipients.txt", "r") as file:
    recipient_emails = file.read().splitlines()

# Loop through the recipient emails and send individual emails
for recipient_email in recipient_emails:
    # Create the email content
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    # Connect to the SMTP server
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, app_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
        server.quit()
        print(f"Email sent to {recipient_email} successfully!")
    except Exception as e:
        print(f"Email to {recipient_email} could not be sent. Error:", str(e))
