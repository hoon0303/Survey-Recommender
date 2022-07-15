from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


app_name = 'survey'

urlpatterns = [
    path('submit', submit, name='submit'),
    path('result', result, name='result'),
    path('', landing),

]