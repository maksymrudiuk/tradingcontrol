#!/usr/bin/python3
from .imageproccesing import init as ipc
# from .models import UploadPhoto
# from report.models import ReportItem, ReportData
from store.models import GoodsInStore, Store
from user.models import UserProfile
from celery import shared_task
from .utils import (name_generator, is_it_processed, perform_update)


@shared_task
def detect(uploadphoto_list, store_id, username):

    goods = GoodsInStore.objects.filter(store_id=store_id)
    store = Store.objects.get(id=store_id)
    user = UserProfile.objects.get(username=username)

    if uploadphoto_list and goods:

        data = {
            'name': name_generator(),
            'store': store,
            'owner': user
        }

        found_list = []

        positiv = 0

        for file in uploadphoto_list:
            for item in goods:

                if is_it_processed(found_list, item.goods.name):
                    continue

                train = file
                query = item.goods.image

                image_status = ipc.init(query, train)

                if image_status:
                    positiv += 1

                data_report_item = {
                    'name': str(item.goods.name),
                    'status': image_status
                }

                found_list = perform_update(found_list, item.goods.name)
                found_list.append(data_report_item)

        goods_percent = round(((positiv / len(goods)) * 100), 2)
        data.update({'assortment_percent': int(goods_percent)})
        data.update({'assortment': found_list})

        return data

    else:
        return 'some error in processing'


@shared_task
def test():
    return 'Celery Works'
