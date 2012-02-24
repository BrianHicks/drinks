'urls for public'
from django.conf.urls.defaults import patterns, url

from drinks.apps.public import views

urlpatterns = patterns('',
    url(r'^$', views.RootView.as_view(), name='root'),
)
