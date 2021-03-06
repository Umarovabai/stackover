from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def send_activation_code(email, code, status):
    if status=='register':
        context = {
            'text_detail': 'Спасибо за регистрацию',
            'email': email,
            'domain': 'http://localhost:8000',
            'code': code
        }
        msg_html = render_to_string('email.html', context)
        message = strip_tags(msg_html)
        send_mail(
            'Активация аккаунта',
            message,
            "stackoverflow_admin@gmail.com",
            [email],
            html_message=msg_html,
            fail_silently=False
        )
    elif status=='forgot_password':
        send_mail(
            'Востановления пароля',
            f"Код активаций: {code}",
            'stackoverflow@admin.com',
            [email],
            fail_silently=True,
        )