'views for public'
from datetime import datetime, timedelta

from django.views.generic.base import View, TemplateResponseMixin

#from drinks.apps.users.models import Profile
from drinks.apps.fluids.models import Drink


class RootView(View, TemplateResponseMixin):
    'the public site'
    template_name = 'index.html'

    def get(self, request):
        'handle GET'
        return self.render_to_response({
            'drinks': Drink.objects.filter(
                when__gte=datetime.now() - timedelta(hours=8)
            )
        })
