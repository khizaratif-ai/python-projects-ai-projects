import os
import ssl
import smtplib
from dotenv import load_dotenv

load_dotenv()


def send_email(message):

    sender = os.getenv("EMAIL_ADDRESS")
    password = os.getenv("EMAIL_PASSWORD")
    receiver = os.getenv("RECEIVER_EMAIL")

    if not sender:
        raise Exception("EMAIL_ADDRESS missing in .env")

    if not password:
        raise Exception("EMAIL_PASSWORD missing in .env")

    if not receiver:
        raise Exception("RECEIVER_EMAIL missing in .env")

    email = f"""Subject: AI News Summary

{message}
"""

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(
        "smtp.gmail.com",
        465,
        context=context
    ) as server:

        server.login(sender, password)

        server.sendmail(
            sender,
            receiver,
            email.encode("utf-8")
        )