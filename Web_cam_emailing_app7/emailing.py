import smtplib
from email.message import EmailMessage
import os


SENDER = "khizaratif657@gmail.com"
PASSWORD = "khce jpvm qzfq rcrm"
PASSWORD = "**** **** **** ****"
RECEIVER = "khizaratif.ai@gmail.com"


def send_email(image_path):

    if not os.path.exists(image_path):
        print("Image not found")
        return


    print("Sending email...")


    email = EmailMessage()

    email["Subject"] = "Security Alert: Person Detected"
    email["From"] = SENDER
    email["To"] = RECEIVER


    email.set_content(
        "A person has been detected by the security camera. Image attached."
    )


    with open(image_path, "rb") as file:

        image_data = file.read()


    email.add_attachment(
        image_data,
        maintype="image",
        subtype="jpeg",
        filename="intruder.jpg"
    )


    try:

        with smtplib.SMTP_SSL(
            "smtp.gmail.com",
            465
        ) as smtp:

            smtp.login(
                SENDER,
                PASSWORD
            )

            smtp.send_message(email)


        print("Email sent successfully!")


    except Exception as error:

        print("Email error:")
        print(error)