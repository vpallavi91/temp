from django.conf.urls import include, url
from django.views.generic import TemplateView

import views
from views import home

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='home'),
    #url(r'^$', 'django_social_app.views.login'),
    url(r'^hello/$', home),
    #url(r'^hello/$', home, name='hello'),
    url(r'', include('social.apps.django_app.urls', namespace='social')),
]
