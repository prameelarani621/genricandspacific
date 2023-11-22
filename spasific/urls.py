from spasific.views import *

from django.urls import path

app_name='anything'

urlpatterns=[
    path('bablu/',bablu,name='bablu'),
    path('hansi/',hansi,name='hansi'),
]