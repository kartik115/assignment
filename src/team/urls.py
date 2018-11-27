from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^team(?:/(?P<member_id>[0-9]+))?/$', team, name='team'),
]