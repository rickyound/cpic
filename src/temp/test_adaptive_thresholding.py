#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 测试自适应阈值化方法的表现

import cv2
import numpy as np
from matplotlib import pyplot as plt

img_gray = cv2.imread('../../sources/sudoku.jpg', 0)
#img_gray = cv2.medianBlur(img_gray, 3)

ret, thresh1 = cv2.threshold(img_gray, 100, 255, cv2.THRESH_BINARY)

thresh2 = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 15, 2)
thresh3 = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, 2)

titles = ['Original Image', 'Simple Thresholding(v=100)', 'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img_gray, thresh1, thresh2, thresh3]

for i in xrange(4):
    plt.subplot(2,2,(i+1)), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
