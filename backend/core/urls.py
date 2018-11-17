from django.urls import path
from .views import Upload

urlpatterns = [
    # Upload photos and set a task on imageprocessing
    path('upload/', Upload.as_view()),
]
