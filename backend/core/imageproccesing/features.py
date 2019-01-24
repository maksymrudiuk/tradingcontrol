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
        # surf = cv2.xfeatures2d.SURF_create()
        sift = cv2.xfeatures2d.SIFT_create()
        # orb = cv2.ORB_create()
        # (self.query_kps, self.query_descs) = surf.detectAndCompute(query, None)
        # (self.train_kps, self.train_descs) = surf.detectAndCompute(train, None)
        # (self.query_kps, self.query_descs) = orb.detectAndCompute(query, None)
        # (self.train_kps, self.train_descs) = orb.detectAndCompute(train, None)
        (self.query_kps, self.query_descs) = sift.detectAndCompute(query, None)
        (self.train_kps, self.train_descs) = sift.detectAndCompute(train, None)

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

    def get_bf_matches(self):
        bf = cv2.BFMatcher()
        matches = bf.knnMatch(self.query_descs, self.train_descs, k=2)

        good = []

        for m, n in matches:
            if m.distance < DISTANCE_CORRECT * n.distance:
                good.append(m)

        matches = sorted(good, key=lambda x: x.distance)
        return matches

    def draw_keypoints(self, img, kps):

        img = cv2.drawKeypoints(img, kps, None, (255, 0, 0), 4)

        plt.figure('Keypoints')
        plt.title('Image')
        plt.imshow(img)
        plt.show()
