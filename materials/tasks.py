from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth import get_user_model

from config.settings import EMAIL_HOST_USER
from materials.models import Subscription


@shared_task
def my_task():
    print('Task executed')


User = get_user_model()


@shared_task
def send_course_update_email(course_id, course_name):
    subscriptions = Subscription.objects.filter(course_id=course_id)
    user_emails = [sub.user.email for sub in subscriptions]

    subject = f'Course "{course_name}" Updated'
    message = f'The course "{course_name}" you are subscribed to has been updated. Please check the latest updates.'

    send_mail(subject, message, EMAIL_HOST_USER, user_emails)
