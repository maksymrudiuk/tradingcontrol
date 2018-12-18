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

# Create your views here.


class ReportListView(APIView):

    authentication_classes = (JSONWebTokenAuthentication,
                              SessionAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):

        time_24_hours_ago = datetime.datetime.now() - datetime.timedelta(days=1)

        if self.request.user.is_superuser:
            context = ReportData.objects.filter(
                created_at__gte=time_24_hours_ago)
        else:
            context = ReportData.objects.filter(
                owner=self.request.user,
                created_at__gte=time_24_hours_ago)

        serializer = ReportDataSerializer(context, many=True)
        return Response(serializer.data)

# Create your views here.
