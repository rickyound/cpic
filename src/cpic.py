#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import cv2

img = cv2.imread('../sources/IMG_20171011_173400.jpg', 0)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

