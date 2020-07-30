from django.urls import path, include
from firstapp import views 

urlpatterns = [
    path('main/', views.main),
    path('show/', views.show),
]
