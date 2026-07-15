import smtplib
from email.message import EmailMessage

PASSWORD = "khce jpvm qzfq rcrm"
SENDER = "khizaratif657@gmail.com"
RECEIVER = "khizaratif.ai@gmail.com"


def send_email(image_path):
    print("Sending email...")

    message = EmailMessage()

    message["Subject"] = "Motion Detected!"
    message["From"] = SENDER
    message["To"] = RECEIVER

    message.set_content("A person is detected in your shop probably a new client!")

    with open(image_path, "rb") as file:
        image_data = file.read()

    message.add_attachment(
        image_data,
        maintype="image",
        subtype="png",
        filename="capture.png",
    )

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
            smtp.starttls()
            smtp.login(SENDER, PASSWORD)
            smtp.send_message(message)

        print("Email sent successfully!")

    except Exception as e:
        print("Email failed:")
        print(e)


if __name__ == "__main__":
    send_email("images/1.png")