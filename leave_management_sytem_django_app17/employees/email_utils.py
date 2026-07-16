from django.conf import settings
from django.core.mail import send_mail


def send_leave_emails(data):
    hr_subject = f"New Leave Application - {data['employee_name']}"

    hr_message = f"""
A new leave application has been submitted.

Employee Name: {data['employee_name']}
Employee ID: {data['employee_id']}
Email: {data['email']}
Department: {data['department']}

Leave Type: {data['leave_type']}
Start Date: {data['start_date']}
End Date: {data['end_date']}

Reason:
{data['reason']}
"""

    send_mail(
        subject=hr_subject,
        message=hr_message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[settings.HR_EMAIL],
        fail_silently=False,
    )

    employee_subject = "Leave Application Received"

    employee_message = f"""
Dear {data['employee_name']},

Your leave application has been submitted successfully.

Application Details

Employee ID: {data['employee_id']}
Department: {data['department']}
Leave Type: {data['leave_type']}
Start Date: {data['start_date']}
End Date: {data['end_date']}

Your request will be reviewed by the HR department.

Thank you.

Best Regards,
HR Department
"""

    send_mail(
        subject=employee_subject,
        message=employee_message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[data["email"]],
        fail_silently=False,
    )