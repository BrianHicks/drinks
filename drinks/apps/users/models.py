"user models"
from datetime import datetime, timedelta

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save


class Profile(models.Model):
    'Profile for a user'
    user = models.OneToOneField(User)

    weight = models.PositiveIntegerField(
        help_text='Your weight, in lbs.',
        default=140,
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
        exercise = 12 * (float(self.exercise) / 30)

        return int(base + exercise)

    def percent_hydrated(self):
        'get percent hydrated'
        total = self.get_water_needed()
        consumed = self.drinks.filter(
            profile=self,
            when__gt=datetime.now() - timedelta(hours=24)
        ).aggregate(models.Sum('amount'))['amount__sum']

        return float(consumed) / total

    def __unicode__(self):
        'unicode representation of this Profile'
        return u'Profile for %s' % self.user


def create_user_profile(sender, instance, created, **kwargs):
    'create a user profile'
    if created:
        Profile.objects.create(user=instance)

post_save.connect(
    create_user_profile, sender=User,
    dispatch_uid='profile_create_on_user'
)
