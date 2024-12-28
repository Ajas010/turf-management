from django.urls import path, include
from turf.views import *

urlpatterns = [
    path('register', register.as_view(), name='turf_register'),
    path('addproduct/', Addproduct.as_view(), name='add_product'),
    path('viewproduct/', Viewproduct.as_view(), name='view_product'),
    path('deleteproduct/<int:id>/', Deleteproduct.as_view(), name='delete_product'),
    path('editproduct/<int:id>/', Editproduct.as_view(), name='edit_product'),
    path('Turfdashboard',Turfdashboard.as_view(),name='loadturf')
      
   
]
    
    