'views for public'
from datetime import datetime, timedelta

from django.views.generic.base import View, TemplateResponseMixin

from drinks.apps.users.models import Profile


class RootView(View, TemplateResponseMixin):
    'the public site'
    template_name = 'index.html'

    def get(self, request):
        'handle GET'
        return self.render_to_response({
            'profiles': Profile.objects.all()
        })
