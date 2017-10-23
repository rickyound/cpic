#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import cv2

img = cv2.imread('../sources/img_small.jpg')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(imgray, 127, 255, 0) 

cv2.namedWindow('original', cv2.WINDOW_NORMAL)
cv2.namedWindow('final', cv2.WINDOW_NORMAL)

cv2.imshow('original', img)
cv2.imshow('final', thresh)

#image, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#cv2.imshow('images', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

