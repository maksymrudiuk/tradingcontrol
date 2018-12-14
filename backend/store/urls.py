from django.urls import path
from . import views

store_list = views.StoreViewSet.as_view({'get': 'list'})
store_detail = views.StoreViewSet.as_view({'get': 'retrieve'})


urlpatterns = [
    path('', store_list),  # Get shop list
    path('<int:pk>/goods/', store_detail)
]
