"user models"
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save


class Profile(models.Model):
    'Profile for a user'
    user = models.OneToOneField(User)

    weight = models.PositiveIntegerField(
        help_text='Your weight, in lbs.'
    )
    exercise = models.PositiveIntegerField(
        help_text='Avg. minutes of exercise, per day'
    )


def create_user_profile(sender, instance, created, **kwargs):
    'create a user profile'
    if created:
        Profile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)
