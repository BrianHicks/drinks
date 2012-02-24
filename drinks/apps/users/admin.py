'admin for users'
from django.contrib import admin
from drinks.apps.users.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    'admin for Profile'

admin.site.register(Profile, ProfileAdmin)
