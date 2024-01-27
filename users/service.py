from django.core.mail import EmailMultiAlternatives
from random import randint


def send_email(code, email):
    html = f"<span>Код для подтверждения почты<span> <h2>{code}<h2>"
    email = EmailMultiAlternatives(
        subject='Подтверждение почты', body=html, to=[email]
    )
    email.attach_alternative(html, "text/html")
    email.send()


def generate_code():
    return randint(1000, 9999)
