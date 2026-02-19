from django.core.mail import send_mail
from django.conf import settings

def send_otp_email(email, otp):
    subject = 'MindCare - OTP Verification'
    message = f'Your OTP for verification is: {otp}'
    from_email = settings.DEFAULT_FROM_EMAIL
    send_mail(subject, message, from_email, [email])

