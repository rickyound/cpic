#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 测试trackbar和Canny边缘检测，使用trackbar来调节minVal和maxVal

import cv2
import numpy as np

img = cv2.imread('../../sources/img_little.jpg', 0)

edges = cv2.Canny(img, 100, 200)

def nothing(x):
    pass

cv2.namedWindow('image')

cv2.createTrackbar('minVal', 'image', 0, 255, nothing)
cv2.createTrackbar('maxVal', 'image', 0, 255, nothing)

while(1):
    cv2.imshow('image', edges)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    minVal = cv2.getTrackbarPos('minVal', 'image')
    maxVal = cv2.getTrackbarPos('maxVal', 'image')

    edges = cv2.Canny(img, minVal, maxVal)

cv2.destroyAllWindows()

