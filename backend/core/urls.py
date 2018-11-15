from django.urls import path
from . import views

urlpatterns = [
    # Upload photos and set a task on imageprocessing
    path('upload/', views.Upload.as_view()),
]
