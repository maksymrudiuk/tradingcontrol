from report.serializers import ReportDataSerializer
from user.models import UserProfile
from .models import UploadPhoto
# from report.models import ReportData


def save_report_in_db(data, store_id, username):
    owner = UserProfile.objects.get(username=username)
    serializer = ReportDataSerializer(data=data)

    if serializer.is_valid():
        serializer.save(owner=owner, store_id=store_id)
        print("ok")
        return(serializer.data['id'])
    else:
        print(serializer.errors)


def update_upload_photo(filename_list, report_id):

    for filename in filename_list:
        photo = UploadPhoto.objects.get(file=filename[7:])
        photo.report_id = report_id
        photo.save()
