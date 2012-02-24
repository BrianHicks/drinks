from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'drinks.views.home', name='home'),
    # url(r'^drinks/', include('drinks.foo.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
