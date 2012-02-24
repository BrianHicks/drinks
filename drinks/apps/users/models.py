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
        help_text='Avg. minutes of exercise, per day',
        default=0,
    )

    def get_water_needed(self):
        'get amount of water in ounces needed per day'
        # weight
        base = float(self.weight) * (2.0 / 3.0)

        # exercise
        excercise += 12 * (float(self.exercise) / 30)

        return int(base + exercise)


def create_user_profile(sender, instance, created, **kwargs):
    'create a user profile'
    if created:
        Profile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)
