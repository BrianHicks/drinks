'admin for fluids'
from django.contrib import admin
from drinks.apps.fluids.models import Drink


class DrinkAdmin(admin.ModelAdmin):
    'admin for Drinks'
    date_hierarchy = 'when'

admin.site.register(Drink, DrinkAdmin)
