from celery import shared_task
from .actions import detect
# from .actions import data_update_after_detect
from .mutations import save_report_in_db


@shared_task
def image_processing(uploadphoto_list, store_id, time_data, username):
    print('image_processing')
    data = detect(uploadphoto_list, store_id)
    data.update(time_data)
    print(data)
    print('SAVE REPORT')
    save_report_in_db(data, store_id, username)
    return 'FINISH'


@shared_task
def test():
    return 'Celery Works'
