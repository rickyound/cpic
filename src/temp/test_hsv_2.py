#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 关于HSV的扩展测试，同时抽取出红色、绿色和蓝色的对象
# Try to find a way to extract more than one colored objects, for eg, extract red, blue, green objects simultaneously.

import cv2
import numpy as np

# 先加载原图
img = cv2.imread('../../sources/colors.jpg', 1)

# 转换HSV色彩空间
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# 分别定义红色、蓝色、绿色的范围
lower_red = np.uint8([0, 100, 100])
upper_red = np.uint8([10, 255, 255])
lower_blue = np.uint8([110, 100, 100])
upper_blue = np.uint8([130, 255, 255])
lower_green = np.uint8([50, 100, 100])
upper_green = np.uint8([70, 255, 255])

# 分别标出三个颜色的范围作为蒙版
mask_red = cv2.inRange(img_hsv, lower_red, upper_red)
mask_blue = cv2.inRange(img_hsv, lower_blue, upper_blue)
mask_green = cv2.inRange(img_hsv, lower_green, upper_green)

# 将三个范围做按位或操作
mask = cv2.bitwise_or(mask_red, mask_blue, mask_green)

# 将原图与最终蒙板进行按位与操作
res = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow('mask_red', mask_red)
cv2.imshow('mask_blue', mask_blue)
cv2.imshow('mask_green', mask_green)
cv2.imshow('mask', mask)
cv2.imshow('res', res)
cv2.waitKey(0)
cv2.destroyAllWindows()
