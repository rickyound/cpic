#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2

img = cv2.imread('../sources/IMG_20171011_173400.jpg', 1)

b, g, r = cv2.split(img)
img = cv2.merge((b, g, r))

# make red pixels all to zero
img[:,:,2] = 0

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

