from rest_framework.response import Response
from .serializers import ReportDataSerializer
from .models import ReportData
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication

# Create your views here.


class ReportListView(APIView):

    authentication_classes = (JSONWebTokenAuthentication,
                              SessionAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):

        if self.request.user.is_superuser:
            context = ReportData.objects.all()
        else:
            context = ReportData.objects.filter(owner=self.request.user)

        serializer = ReportDataSerializer(context, many=True)
        return Response(serializer.data)

# Create your views here.
