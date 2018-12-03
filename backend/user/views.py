from rest_framework.response import Response
from .serializers import UserProfileSerializer
from .models import UserProfile
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication

# Create your views here.


class GetUserProfile(APIView):

    authentication_classes = (JSONWebTokenAuthentication,
                              SessionAuthentication)

    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        user = UserProfile.objects.get(username=request.user)
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)
