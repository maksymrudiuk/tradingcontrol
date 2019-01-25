# Standart Library Modules
import os
# import time
# from collections import defaultdict

# Download Modules
import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import cv2.cv2 as cv2

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

    path = str(train_path)[7:]
    train_p = os.path.join(settings.MEDIA_ROOT, path)
    # train_p = os.path.join(path)
    # print(train_p)
    train = mpimg.imread(train_p)

    # Get matches and keypoints
    features = Features(query, train)
    # query_kps, train_kps = features.get_kps()
    # query_descs, train_descs = features.get_descs()
    # matches = features.get_matches()
    matches = features.get_bf_matches()

    if len(matches) < MATCH_THRESHOLD:
        # print(len(matches))
        status = False
        # print('False')

    else:
        # print(len(matches))
        # print('True')
        # r_table = build_r_table(query, query_kps, matches, reference_point)
        # accumulator = accumulate_kps(r_table, train, train_kps, matches)
        # src_pts = np.float32([query_kps[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)
        # dst_pts = np.float32([train_kps[m.trainIdx].pt for m in matches]).reshape(-1, 1, 2)

        # (M, mask) = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
        # matchesMask = mask.ravel().tolist()
        # (h, w) = query.shape[:-1]
        # pts = np.float32([[0, 0], [0, h - 1],
        #                  [w - 1, h - 1], [w - 1, 0]]).reshape(-1, 1, 2)
        # dst = cv2.perspectiveTransform(pts, M)

        # train = cv2.polylines(train, [np.int32(dst)],
        #                       True, (255, 0, 0), 3, cv2.LINE_AA)

        # draw_params = dict(matchColor=(0, 255, 0),
        #                    singlePointColor=None,
        #                    # matchesMask=matchesMask,
        #                    flags=2)

        # img3 = cv2.drawMatches(query, query_kps,
        #                        train, train_kps, matches,
        #                        None, **draw_params)
        # plt.ioff()
        # plt.figure('Res')
        # plt.imshow(img3)
        # plt.show()
        status = True
    return status
