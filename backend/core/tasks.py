from celery import shared_task
from .actions import detect
# from .actions import data_update_after_detect
from .mutations import save_report_in_db, update_upload_photo


@shared_task
def image_processing(uploadphoto_list, store_id, time_data, username):
    data = detect(uploadphoto_list, store_id)
    print(data)
    if data:
        data.update(time_data)
        report_id = save_report_in_db(data, store_id, username)
        update_upload_photo(uploadphoto_list, report_id)
        print('All operations in successfuly completed')
    else:
        print('Error in detect process')


@shared_task
def test():
    return 'Celery Works'
