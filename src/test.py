#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np

img01 = cv2.imread('../sources/opencv-logo.jpg', 1)
img02 = cv2.imread('../sources/ewm.jpg', 1)

timg01 = cv2.add(img01, img02)
timg02 = img01 + img02

cv2.namedWindow('image1', cv2.WINDOW_NORMAL)
cv2.namedWindow('image2', cv2.WINDOW_NORMAL)
cv2.imshow('image1', timg01)
cv2.imshow('image2', timg02)
cv2.waitKey(0)
cv2.destroyAllWindows()

