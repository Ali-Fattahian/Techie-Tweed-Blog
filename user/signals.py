from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from .models import Profile

def create_profile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(user = user, email = user.email)

        subject = 'Welcome to Techie Tweed'
        message = 'We are honored to see you as our new member!'
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [user.email],
            fail_silently= False
        )


post_save.connect(create_profile, sender = User)
