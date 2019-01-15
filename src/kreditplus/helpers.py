"""
Helpers
=======

Utility functions which are used in other modules.
"""
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# def installment_calculation(order_request):
    # TODO:
    #   1. Get tenor
    #   2. Calculate installment


def build_message(sender, recipients, subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ",".join(recipients)

    return msg


def send_message(mail_server, mail_port, mail_username, mail_password, msg):
    s = smtplib.SMTP(mail_server, mail_port)
    s.starttls()
    s.login(mail_username, mail_password)

    result = s.sendmail(msg["From"], msg["To"].split(","), msg.as_string())
    s.quit()

    return result

