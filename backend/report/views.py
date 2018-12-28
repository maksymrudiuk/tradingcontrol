# Standart library
import datetime
# Rest library
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication

# Locale modules
from .serializers import ReportDataSerializer
from .models import ReportData
from user.models import UserProfile

# Create your views here.


class ReportListView(APIView):

    authentication_classes = (JSONWebTokenAuthentication,
                              SessionAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):

        days = int(self.request.query_params['fordays'])
        time_ago = datetime.datetime.now() - datetime.timedelta(days=days)

        if self.request.user.isDirector:
            staff = UserProfile.objects.filter(
                company=self.request.user.company)
            context = ReportData.objects.filter(
                owner__in=staff,
                created_at__gte=time_ago)

        else:
            context = ReportData.objects.filter(
                owner=self.request.user,
                created_at__gte=time_ago)

        serializer = ReportDataSerializer(context, many=True)
        return Response(serializer.data)

# Create your views here.
