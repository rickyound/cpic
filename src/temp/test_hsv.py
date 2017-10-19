#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ����HSV����ȡ��ɫ����

import cv2
import numpy as np

# ��ȡԭͼ
img = cv2.imread('../../sources/castle.jpg', 1)

# ��ԭͼת��ΪHSVɫ�ʿռ�
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# ������HSV�л�ɫ�ķ�Χ
lower_yellow = np.uint8([0, 50, 50])
upper_yellow = np.uint8([34, 255, 255])

# Ӧ��HSVͼ���ɫ��ֵ��ȡ��ɫͼ����Ϊ�ɰ�
mask = cv2.inRange(img_hsv, lower_yellow, upper_yellow)

# ��ԭͼ���ɰ水λ������õ�Ŀ��ͼ
res = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow('img', img)
cv2.imshow('img_hsv', img_hsv)
cv2.imshow('mask', mask)
cv2.imshow('res', res)

cv2.waitKey(0)
cv2.destroyAllWindows()
