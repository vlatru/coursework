from django.conf.urls import patterns, include, url
from quiz.views import *
from quiz import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns(
    '',
    url(r'^$', index),
    url(r'^quiz/(?P<que_id>\d+)/$', quiz),
    url(r'^stats/(?P<que_id>\d+)/$', stats),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.STATIC_ROOT, }),
)
