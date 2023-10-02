# Auto Email Script

## Overview

This Python script allows you to send automated emails using Gmail SMTP. It's a simple and versatile tool that can be used for sending bulk emails or automating email notifications.

## Prerequisites

Before using this script, make sure you have the following:

- Python installed on your system (Python 3.x recommended).
- A Gmail account (with Two-Factor Authentication).

## Setup

1. Clone this repository to your local machine:
   git clone https://github.com/Parthpatil7/Auto-Email-Script.git
2. Navigate to the project directory:
   cd Auto-Email-Script
3. Open the script (autoemail.py) in a text editor and configure the following:
   sender_email: Your Gmail email address.
   password: Your Gmail App Password (2FA is enabled).
   Customize the email message, subject, and other details.
4. To send emails, you can use the following command:
   python autoemail.py


The script will read recipient email addresses from a text file (recipients.txt) and send emails to each recipient.

Configuration
sender_name: You can change the name displayed in the "From" field of the email.
recipient_emails: Add recipient email addresses to the recipients.txt file, one per line.
Security Note
You are required to have Two-Factor Authentication (2FA) enabled on your Gmail account, generate an App Password for secure access.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Python - The programming language used.
smtplib - Python's SMTP library for sending emails.
Feel free to report any issues.

Happy emailing!
