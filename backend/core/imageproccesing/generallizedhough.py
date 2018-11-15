# Standart Library Modules
import math
from collections import defaultdict
# import time

# Download Modules
import numpy as np
import cv2.cv2 as cv2
# import matplotlib.pyplot as plt

# Local Modules
from .settings import BIN_SIZE


def build_r_table(query, query_kps, matches, reference_point):

    r_table = defaultdict(list)
    x0, y0 = reference_point

    for m in matches:

        kp = query_kps[m.queryIdx]
        (x, y) = kp.pt
        # theta = kp.angle

        beta = math.degrees(math.atan((x - x0 / y - y0)))
        rho = math.sqrt(math.pow((x - x0), 2) + math.pow((y - y0), 2))

        r_table[kp].append((beta, rho))

    return r_table


def accumulate_kps(r_table, train, train_kps, matches):

    h, w = train.shape[:2]

    max_scale = 2.1
    delta_theta = 10
    delta_scale = 0.1

    angle = int(360 // delta_theta) + 1
    scale = int(max_scale // delta_scale) + 1

    h = int(h / BIN_SIZE) + 1
    w = int(w / BIN_SIZE) + 1

    accumulator = np.zeros((h, w, angle, scale), dtype=int)
    kps = np.array([train_kps[m.trainIdx] for m in matches])

    for kp in kps:

        (x, y) = kp.pt

        for r in r_table:
            [(alpha, rho)] = r_table[r]
            for theta in range(0, 361, 20):
                for s in np.arange(0.1, max_scale, delta_scale):

                    x0 = x + rho * s * math.cos(alpha + theta)
                    y0 = y + rho * s * math.sin(alpha + theta)

                    x_acc, y_acc = int(x0 / BIN_SIZE), int(y0 / BIN_SIZE)

                    if 0 < x_acc < w and 0 < y_acc < h:
                        accumulator[y_acc][x_acc][int(theta // delta_theta)][int(s // delta_scale)] += 1

    return accumulator


def draw_segment(accumulator, train, title):

    (i, j, m, n) = np.unravel_index(accumulator.argmax(), accumulator.shape)

    (y0, x0) = (i * BIN_SIZE, j * BIN_SIZE)
    (y1, x1) = (y0 + BIN_SIZE, x0 + BIN_SIZE)

    cv2.rectangle(train, (x0, y0), (x1, y1), (255, 0, 0), 3)
    # cv2.imwrite(title + '.png', img)
    return train
