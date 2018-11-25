import string
import random


def name_generator(size=10, chars=string.ascii_letters + string.digits):
    return ''.join(random.SystemRandom().choice(chars) for _ in range(size))


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
