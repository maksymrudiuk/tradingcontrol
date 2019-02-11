from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication

from .serializers import UserProfileSerializer
from .models import UserProfile

# Create your views here.


class GetUserProfile(APIView):

    authentication_classes = (JSONWebTokenAuthentication,
                              SessionAuthentication)

    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        user = UserProfile.objects.get(username=self.request.user)
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)


class StaffView(APIView):

    authentication_classes = (JSONWebTokenAuthentication,
                              SessionAuthentication)

    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):

        if self.request.user.isDirector:
            staff = UserProfile.objects.filter(
                company=self.request.user.company).exclude(
                    username=self.request.user)
            serializer = UserProfileSerializer(staff, many=True)
        else:
            user = UserProfile.objects.get(username=self.request.user)
            serializer = UserProfileSerializer(user)
        return Response(serializer.data)
