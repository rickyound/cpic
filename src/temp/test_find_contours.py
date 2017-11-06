#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ≤‚ ‘—∞’“ÕºœÒµƒ¬÷¿™

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../../sources/castle.jpg')

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(img_gray, 127, 255, 0)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

img_rel = cv2.drawContours(img_gray, contours, -1, (0, 255, 0), 3)

print cv2.drawContours(img_gray, contours, -1, (0, 255, 0), 3)
#cv2.imshow('img_rel', img_rel)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
