# Standart Library Modules
import os
# import time
# from collections import defaultdict

# Download Modules
# import numpy as np
import matplotlib.image as mpimg
# import matplotlib.pyplot as plt
# import cv2.cv2 as cv2

# Local Modules
from .settings import *
from .features import Features
# from .generallizedhough import build_r_table, accumulate_kps
from django.conf import settings


def init(query_path, train_path):

    query_p = os.path.join(settings.MEDIA_ROOT, str(query_path))
    query = mpimg.imread(query_p)

    # h, w = query.shape[:2]

    # y = int(h // 2)
    # x = int(w // 2)
    # reference_point = (x, y)

    path = str(train_path)
    train_p = os.path.join(settings.MEDIA_ROOT, path)
    train = mpimg.imread(train_p)

    # Get matches and keypoints
    features = Features(query, train)
    # query_kps, train_kps = features.get_kps()
    # query_descs, train_descs = features.get_descs()
    matches = features.get_matches()

    if len(matches) < MATCH_THRESHOLD:
        status = False

    else:

        # r_table = build_r_table(query, query_kps, matches, reference_point)
        # accumulator = accumulate_kps(r_table, train, train_kps, matches)
        status = True
    return status
