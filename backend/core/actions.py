from .imageproccesing import init as ipc
from .utils import name_generator
from store.models import GoodsInStore


def is_it_processed(found_list, current_item):

    '''
    This function watch: which files has been
    processing and found in the picture
    '''

    for item in found_list:

        if item['name'] == current_item and item['status']:
            return True


def perform_update(found_list, current_item):

    response_list = []

    for item in found_list:
        if item['name'] == current_item and not item['status']:
            del item
        else:
            response_list.append(item)

    return response_list


def detect(uploadphoto_list, store_id):

    goods = GoodsInStore.objects.filter(store_id=int(store_id))

    if uploadphoto_list and goods:

        data = {
            'name': name_generator(),
        }

        found_list = []

        positiv = 0

        for file in uploadphoto_list:

            for item in goods:

                if is_it_processed(found_list, item.goods.name):
                    continue

                train = file
                query = item.goods.image

                try:
                    image_status = ipc.init(query, train)
                except Exception:
                    continue

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
        return False
