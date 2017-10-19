#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ����HSV����չ���ԣ�ͬʱ��ȡ����ɫ����ɫ����ɫ�Ķ���
# Try to find a way to extract more than one colored objects, for eg, extract red, blue, green objects simultaneously.

import cv2
import numpy as np

# �ȼ���ԭͼ
img = cv2.imread('../../sources/colors.jpg', 1)

# ת��HSVɫ�ʿռ�
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# �ֱ����ɫ����ɫ����ɫ�ķ�Χ
lower_red = np.uint8([0, 100, 100])
upper_red = np.uint8([10, 255, 255])
lower_blue = np.uint8([110, 100, 100])
upper_blue = np.uint8([130, 255, 255])
lower_green = np.uint8([50, 100, 100])
upper_green = np.uint8([70, 255, 255])

# �ֱ���������ɫ�ķ�Χ��Ϊ�ɰ�
mask_red = cv2.inRange(img_hsv, lower_red, upper_red)
mask_blue = cv2.inRange(img_hsv, lower_blue, upper_blue)
mask_green = cv2.inRange(img_hsv, lower_green, upper_green)

# ��������Χ����λ�����
mask = cv2.bitwise_or(mask_red, mask_blue, mask_green)

# ��ԭͼ�������ɰ���а�λ�����
res = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow('mask_red', mask_red)
cv2.imshow('mask_blue', mask_blue)
cv2.imshow('mask_green', mask_green)
cv2.imshow('mask', mask)
cv2.imshow('res', res)
cv2.waitKey(0)
cv2.destroyAllWindows()
