#!/usr/bin/python3
from .imageproccesing import init as ipc
from .models import UploadPhoto, ReportData, ReportItem, Goods
from celery import shared_task


@shared_task
def detect(uploadphoto_id, shop_id):

    imgs = Goods.objects.filter(shop_id=shop_id)
    photo = UploadPhoto.objects.get(id=uploadphoto_id)
    if photo:
        train = photo.photo
        report_data = {'name': str(train)[:7]}
        report = ReportData(**report_data)
        report.assortment_id = shop_id
        report.save()

        if imgs:
            for img in imgs:

                query = img.image
                print(train)
                image_status = ipc.init(query, train)
                data_report_item = {'name': img.name}

                if image_status:
                    data_report_item['status'] = 'found'
                else:
                    data_report_item['status'] = 'not found'

                report_item = ReportItem(**data_report_item)
                report_item.report_id = report.id
                report_item.save()

        return 'end'

    else:
        return 'error'


@shared_task
def test():
    return 'Celery Works'
