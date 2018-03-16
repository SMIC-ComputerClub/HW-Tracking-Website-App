from django.conf.urls import url

from . import views

app_name = 'log'
urlpatterns = [
    url(r'^(?P<course_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^reminder/$', views.reminder, name = 'reminder'),
]
