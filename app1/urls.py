from app1.views import *
from django.urls import path
app_name='csk'
urlpatterns=[
    path('csk/',csk,name='csk'),
]