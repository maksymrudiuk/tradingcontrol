from django.urls import path
from .views import (ManagerRegisterView,
                    GeneralManagerRegisterView,
                    GetRegisterKeyView)
from rest_auth.registration.views import VerifyEmailView


urlpatterns = [
    # path('', include('rest_auth.urls')),
    path('manager-signup/', ManagerRegisterView.as_view()),
    path('general-manager-signup/', GeneralManagerRegisterView.as_view()),
    path('verify-email/', VerifyEmailView.as_view()),
    path('verify-person/', GetRegisterKeyView.as_view()),
]
