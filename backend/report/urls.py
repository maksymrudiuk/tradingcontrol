from django.urls import path
from . import views
from core.views import GetStorePhotosViewSet

reports_list = views.ReportViewSet.as_view({'get': 'list'})
report_detail = views.ReportViewSet.as_view({'get': 'retrieve'})

report_detail_images = GetStorePhotosViewSet.as_view({'get': 'retrieve'})

urlpatterns = [
    path('', reports_list),
    path('<int:pk>/detail/', report_detail),
    path('<int:pk>/detail/images/', report_detail_images),
]
