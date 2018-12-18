# Standart Library
import string
import random


def name_generator(size=6, chars=string.ascii_letters + string.digits):
    slug_id = ''.join(random.SystemRandom().choice(chars) for _ in range(size))
    return 'report_' + (slug_id)
