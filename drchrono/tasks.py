from __future__ import absolute_import, unicode_literals
from celery import shared_task

from celery.task.schedules import crontab
from celery.decorators import periodic_task
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context


@periodic_task(run_every=(crontab()), name="some_task", ignore_result=True)
def some_task():
    print("palllooooooooo!!")

@periodic_task(run_every=(crontab(minute='*/1')), name="some_task1", ignore_result=True)
def some_task1():
    plaintext = get_template('email.txt')
    htmly     = get_template('email.html')

    d = Context({ 'username': 'pallo' })

    subject, from_email, to = 'hello', 'vpallavi91@gmail.com', ['prankypallo@gmail.com','pallavijayakumar91@gmail.com']
    text_content = plaintext.render(d)
    html_content = htmly.render(d)
    msg = EmailMultiAlternatives(subject, text_content, from_email, to)
    msg.attach_alternative(html_content, "text/html")
    msg.send()
