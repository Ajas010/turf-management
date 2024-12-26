from django.urls import path

from .views import *

urlpatterns = [
   
   path('turf_approval/',AdminTurfApprovalView.as_view(),name='admin_turf_approval'),
   path('adminviewuser/',adminviewuser.as_view(),name='adminviewuser'),
   path('adminviewturf/',adminviewturf.as_view(),name='adminviewtur'),
   path('adminviewbooking/',adminviewbooking.as_view(),name='adminviewbooking'),
   path('adminviewproduct/',adminviewproduct.as_view(),name='adminviewproduct'),
   path('adminviewrenting/',adminviewrenting.as_view(),name='adminviewrenting'),



   # path('addproduct/', Addproduct.as_view(), name='add_product'),
   # path('viewproduct/', Viewproduct.as_view(), name='view_product'),
   # path('deleteproduct/<int:id>/', Deleteproduct.as_view(), name='delete_product'),
   # path('editproduct/<int:id>/', Editproduct.as_view(), name='edit_product')
]
    