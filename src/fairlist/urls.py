from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
     path('auth/', include('djoser.urls')),
     path('auth/', include('djoser.urls.authtoken')),
     path('items/', views.ItemList.as_view(), name='items'),
     path('items/<int:pk>', views.ItemDetail.as_view(), name='itemDetail'),
]
