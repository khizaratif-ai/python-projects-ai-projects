import smtplib
import config

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(receiver, message):

    email = MIMEMultipart()

    email["From"] = config.EMAIL
    email["To"] = receiver
    email["Subject"] = "Latest News Update"


    email.attach(
        MIMEText(
            message,
            "plain",
            "utf-8"
        )
    )


    server = smtplib.SMTP(
        "smtp.gmail.com",
        587
    )


    server.starttls()


    server.login(
        config.EMAIL,
        config.PASSWORD
    )


    server.sendmail(
        config.EMAIL,
        receiver,
        email.as_string()
    )


    server.quit()