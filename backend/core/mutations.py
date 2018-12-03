from report.serializers import ReportDataSerializer
from user.models import UserProfile


def save_report_in_db(data, store_id, username):
    owner = UserProfile.objects.get(username=username)
    serializer = ReportDataSerializer(data=data)

    if serializer.is_valid():
        serializer.save(owner=owner, store_id=store_id)
        return serializer.data
    else:
        return serializer.errors
