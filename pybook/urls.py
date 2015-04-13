from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),  # noqa
    url(r'^blog/', include('blog.urls', namespace='blog')),
)
