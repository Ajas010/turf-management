from django.urls import path, include

from turf.views import *

urlpatterns = [
    path('login', LoginPage.as_view(), name='login'),
    
   
]
