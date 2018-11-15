# Standart Library Modules
# import os

# Download Modules
import cv2.cv2 as cv2
# import numpy as np
# import matplotlib.image as mpimg
import matplotlib.pyplot as plt

# Local Modules
from .settings import *


class Features(object):
    """docstring for Features"""

    def __init__(self, query, train):
        # super(Features, self).__init__()
        surf = cv2.xfeatures2d.SURF_create()
        (self.query_kps, self.query_descs) = surf.detectAndCompute(query, None)
        (self.train_kps, self.train_descs) = surf.detectAndCompute(train, None)

    def get_kps(self):
        return (self.query_kps, self.train_kps)

    def get_descs(self):
        return (self.query_descs, self.train_descs)

    def get_matches(self):

        FLANN_INDEX_KDTREE = 0
        index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
        search_params = dict(checks=50)

        flann = cv2.FlannBasedMatcher(index_params, search_params)

        matches = flann.knnMatch(self.query_descs, self.train_descs, k=2)

        self.good = []

        for m, n in matches:
            if m.distance < DISTANCE_CORRECT * n.distance:
                self.good.append(m)

        return self.good

    def draw_keypoints(self, img, kps):

        img = cv2.drawKeypoints(img, kps, None, (255, 0, 0), 4)

        plt.figure('Keypoints')
        plt.title('Image')
        plt.imshow(img)
        plt.show()
