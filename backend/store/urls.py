from django.urls import path
from . import views

urlpatterns = [
    path('stores/', views.ShopList.as_view()),  # Get shop list
]
