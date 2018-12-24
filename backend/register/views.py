from uuid import uuid4
from django.core.mail import EmailMessage
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import RegisterKeyEmailSerialiazer
from .models import RegisterKey
from rest_auth.registration.views import RegisterView

# Create your views here.


class ManagerRegisterView(RegisterView):

    def dispatch(self, *args, **kwargs):
        return super(ManagerRegisterView, self).dispatch(*args, **kwargs)

    def perform_create(self, serializer):
        user = super(ManagerRegisterView, self).perform_create(serializer)
        user.is_manager = True
        user.save()
        return user


class GeneralManagerRegisterView(RegisterView):

    def perform_create(self, serializer):
        user = super(GeneralManagerRegisterView, self).perform_create(serializer)
        user.is_general_manager = True
        user.save()
        return user


class GetRegisterKeyView(APIView):

    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = RegisterKeyEmailSerialiazer(request.data)
        email = serializer.data['email']
        key = str(uuid4().int)[:6]
        rgk = RegisterKey(key=key, email=email)
        rgk.save()
        msg = EmailMessage('Observer Project',
                           'PIN для реєстрації: %s' % key,
                           'from@example.com',
                           [email])
        msg.send()
        return Response(serializer.data)
