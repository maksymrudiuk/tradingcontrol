from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.ReportListView.as_view()),  # Get report list
]
