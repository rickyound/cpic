#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np

img01 = cv2.imread('../sources/opencv-logo.jpg', 1)
img02 = cv2.imread('../sources/ewm.jpg', 1)

dst = cv2.addWeighted(img01, 0.7, img02, 0.3, 0)

cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
cv2.imshow('image', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

