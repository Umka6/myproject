from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='home'),
    path('applications/', ApplicationsView.as_view(), name='applications'),
]