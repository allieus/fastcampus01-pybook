from django.conf.urls import patterns, url


urlpatterns = patterns('blog.views',
    url(r'^$', 'index', name='index'),  # noqa
    url(r'^new/$', 'new', name='new'),
    url(r'^(?P<id>\d+)/$', 'detail', name='detail'),
    url(r'^(?P<id>\d+)/edit/$', 'edit', name='edit'),
    url(r'^(?P<id>\d+)/delete/$', 'delete', name='delete'),
)
