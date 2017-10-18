#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import cv2
import time

img1 = cv2.imread('../sources/opencv-logo.jpg')
img2 = cv2.imread('../sources/castle.jpg')

img1_rows, img1_cols, img1_channels = img1.shape
img2_rows, img2_cols, img2_channels = img2.shape

min_rows = img1_rows if img1_rows <= img2_rows else img2_rows
min_cols = img1_cols if img1_cols <= img2_cols else img2_cols

img1_ori = img1[0:min_rows, 0:min_cols]
img2_ori = img2[0:min_rows, 0:min_cols]

img = cv2.addWeighted(img1_ori, 0.7, img2_ori, 0.3, 0)

cv2.namedWindow('image', cv2.WINDOW_NORMAL)

img2[0:min_rows, 0:min_cols] = img
cv2.imshow('image', img2)

cv2.waitKey(0)
cv2.destroyAllWindows()

