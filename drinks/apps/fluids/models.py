'models for fluids'
from django.db import models


class Drink(models.Model):
    'a single drink (drink, whatever)'
    profile = models.ForeignKey(
        'users.Profile',
        related_name='drinks'
    )

    amount = models.PositiveIntegerField(
        help_text='Fluid amount, in oz.'
    )
    kind = models.CharField(
        max_length=50,
        help_text='Kind of fluid (water, tea, coffee, etc.)'
    )
    when = models.DateTimeField(auto_now_add=True)
