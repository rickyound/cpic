#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2

img = cv2.imread('../sources/IMG_20171011_173400.jpg', 1)

flag = img[646:1282, 2466:3046]
img[646:1282, 1466:2046] = flag

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

