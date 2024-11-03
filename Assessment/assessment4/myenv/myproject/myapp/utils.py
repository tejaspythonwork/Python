# policies/utils.py
from django.core.mail import send_mail
from django.conf import settings

def send_confirmation_email(email, approved=False):
    if approved:
        subject = "Policy Approval Confirmation"
        message = "Congratulations! Your policy has been approved."
    else:
        subject = "Policy Request Received"
        message = "Thank you for requesting a policy. We will process it soon."
    
    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
    )
