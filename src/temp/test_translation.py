#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ²âÊÔÍ¼Ïñ×ª»»

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../../sources/castle.jpg')

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

rows, cols = img_gray.shape

M = np.float32([[1, 0, 100], [0, 1, 50]])
dst = cv2.warpAffine(img_gray, M, (cols, rows))

cv2.imshow('img_gray', img_gray)
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
