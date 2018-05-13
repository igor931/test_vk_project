from django.conf.urls import url, include
from post.views import *

urlpatterns = [
	url(r'^$', Index.as_view(), name='index'),
    url(r'get/$', get_obj, name='get_object'),
    url(r'^login/', login),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^(?P<slug>[-\w]+)/$', group_posts, name='group_posts'),
    #url(r'^social/$', include('social_auth_urls')),
    url(r'^social/', include('social.apps.django_app.urls', namespace='social')),
    
]