#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np

# 加载两幅图片
img01 = cv2.imread('../sources/castle.jpg', 1)
#img02 = cv2.imread('../sources/opencv-logo.jpg', 1)
# 此图用背景为透明的来做方便一些，所以要用opencv-log-white.png图片，自己截图的有蓝色背景
img02 = cv2.imread('../sources/opencv-logo-white.png', 1)

# 因为需要将logo置于左上角，所以根据img02的尺寸创建一个ROI
rows, cols, channels = img02.shape
roi = img01[0:rows, 0:cols]

# 现在创建一个logo的蒙版和它的反转蒙版
img02gray = cv2.cvtColor(img02, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img02gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

# 然后将logo中的ROI进行遮光
img01_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

# 仅从logo中取出logo部分
img02_bg = cv2.bitwise_and(img02, img02, mask=mask)

# 将logo放入ROI中，并且修改主图中相应区域
dst = cv2.add(img01_bg, img02_bg)
img01[0:rows, 0:cols] = dst

# 展示看效果
cv2.imshow('img02gray', img02gray)
cv2.imshow('img02mask', mask)
cv2.imshow('image', img01)
cv2.waitKey(0)
cv2.destroyAllWindows()

