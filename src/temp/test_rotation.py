#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 测试图像旋转

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../../sources/castle.jpg', 0)
rows, cols = img.shape

# 参数旋转坐标、角度、缩放比例
M = cv2.getRotationMatrix2D((cols/2, rows/2), 90, 1)
print M
dst = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow('img', img)
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
