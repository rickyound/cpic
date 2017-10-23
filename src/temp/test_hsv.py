#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 测试HSV来提取颜色对象

import cv2
import numpy as np

# 读取原图
img = cv2.imread('../../sources/castle.jpg', 1)

# 将原图转换为HSV色彩空间
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# 定义在HSV中黄色的范围
lower_yellow = np.uint8([0, 50, 50])
upper_yellow = np.uint8([34, 255, 255])

# 应用HSV图像黄色阈值获取黄色图像作为蒙版
mask = cv2.inRange(img_hsv, lower_yellow, upper_yellow)

# 将原图和蒙版按位与操作得到目标图
res = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow('img', img)
cv2.imshow('img_hsv', img_hsv)
cv2.imshow('mask', mask)
cv2.imshow('res', res)

cv2.waitKey(0)
cv2.destroyAllWindows()
