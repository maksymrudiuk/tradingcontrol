#!/usr/bin/python3
# from .imageproccesing import init as ipc
from .models import UploadPhoto
# from report.models import ReportItem, ReportData
# from goods.models import Goods
from store.models import GoodsInStore
from celery import shared_task


@shared_task
def detect(uploadphoto_id, store_id):

    goods = GoodsInStore.objects.filter(store_id=store_id)
    for item in goods:
        print(item.goods.image)
    obj = UploadPhoto.objects.get(id=uploadphoto_id)
    print(obj.file)

    # if obj:
    #     train = obj.file
    #     report_data = {'name': str(train)[:7]}
    #     report = ReportData(**report_data)
    #     report.assortment_id = store_id
    #     report.save()

    #     if imgs:
    #         for img in imgs:

    #             query = img.image
    #             print(train)
    #             image_status = ipc.init(query, train)
    #             data_report_item = {'name': img.name}

    #             if image_status:
    #                 data_report_item['status'] = 'found'
    #             else:
    #                 data_report_item['status'] = 'not found'

    #             report_item = ReportItem(**data_report_item)
    #             report_item.report_id = report.id
    #             report_item.save()

    #     return 'end'

    # else:
    #     return 'error'


@shared_task
def test():
    return 'Celery Works'
