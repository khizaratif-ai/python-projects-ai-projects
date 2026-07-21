import smtplib
from email.message import EmailMessage

# Sender Email Configuration
EMAIL_ADDRESS = "ENTER_YOUR_EMAIL"
EMAIL_PASSWORD = "ENTER_YOUR_16_DIGITS_PASSWORD"


def send_email(receiver_email, first_name, start_date, confirmation_link):
    """
    Sends a confirmation email to the applicant.
    """

    message = EmailMessage()

    message["Subject"] = "Job Application Submitted Successfully"
    message["From"] = EMAIL_ADDRESS
    message["To"] = receiver_email

    message.set_content(f"""
Dear {first_name},

Thank you for applying.

Your job application has been submitted successfully.

----------------------------------------------------

Applicant Name:
{first_name}

Expected Start Date:
{start_date}

----------------------------------------------------

To view your application confirmation, please click the link below:

{confirmation_link}

If the link does not open automatically, copy and paste it into your browser.

For further enquiries, please contact:

khizaratif657@gmail.com

We appreciate your interest and wish you the very best.

Kind Regards,

Khizar Atif
Recruitment Team
""")

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(message)

        print("Email sent successfully.")

    except Exception as error:
        print("Unable to send email.")
        print(error)
