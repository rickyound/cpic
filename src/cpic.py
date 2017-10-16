#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import cv2
from matplotlib import pyplot as plt

img = cv2.imread('../sources/IMG_20171011_173400.jpg', 0)

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('images', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

