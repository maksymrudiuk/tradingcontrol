# Standart library
import datetime
# Rest library
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication

# Locale modules
from .serializers import ReportDataGETSerializer
from .models import ReportData
from user.models import UserProfile

# Create your views here.


# class ReportListView(APIView):

#     authentication_classes = (JSONWebTokenAuthentication,
#                               SessionAuthentication,)
#     permission_classes = (IsAuthenticated,)

#     def get(self, request, format=None):

#         filter_params = {}

#         if 'fordays' in self.request.query_params:
#             days = int(self.request.query_params['fordays'])
#             time_ago = datetime.datetime.now() - datetime.timedelta(days=days)
#             filter_params['created_at__gte'] = time_ago

#         if 'store' in self.request.query_params:
#             store = int(self.request.query_params['store'])
#             filter_params['store__id'] = store

#         if self.request.user.isDirector:

#             staff = UserProfile.objects.filter(
#                 company=self.request.user.company)

#             context = ReportData.objects.filter(
#                 owner__in=staff,
#                 **filter_params)

#         else:
#             context = ReportData.objects.filter(
#                 owner=self.request.user,
#                 **filter_params)

#         serializer = ReportDataSerializer(context, many=True)
#         return Response(serializer.data)

class ReportViewSet(viewsets.ViewSet):

    authentication_classes = (JSONWebTokenAuthentication,
                              SessionAuthentication,)
    permission_classes = (IsAuthenticated,)

    def list(self, request, format=None):

        filter_params = {}

        if 'fordays' in self.request.query_params:
            days = int(self.request.query_params['fordays'])
            time_ago = datetime.datetime.now() - datetime.timedelta(days=days)
            filter_params['created_at__gte'] = time_ago

        if 'store' in self.request.query_params:
            store = int(self.request.query_params['store'])
            filter_params['store__id'] = store

        if self.request.user.isDirector:

            staff = UserProfile.objects.filter(
                company=self.request.user.company)

            context = ReportData.objects.filter(
                owner__in=staff,
                **filter_params)

        else:
            context = ReportData.objects.filter(
                owner=self.request.user,
                **filter_params)

        serializer = ReportDataGETSerializer(context, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = ReportData.objects.get(id=pk)
        serializer = ReportDataGETSerializer(queryset)
        return Response(serializer.data)

# Create your views here.
