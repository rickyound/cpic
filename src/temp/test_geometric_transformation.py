#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 测试图像的几何转换

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../../sources/castle.jpg', 1)

#res = cv2.resize(img, None, fx=1, fy=2, interpolation=cv2.INTER_CUBIC)

height, width = img.shape[:2]
res = cv2.resize(img, (width*2, height*2), interpolation=cv2.INTER_CUBIC)

cv2.imshow('res', res)
cv2.waitKey(0)
cv2.destroyAllWindows()

