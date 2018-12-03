# Standart Library
import string
import random


def name_generator(size=10, chars=string.ascii_letters + string.digits):
    return ''.join(random.SystemRandom().choice(chars) for _ in range(size))
