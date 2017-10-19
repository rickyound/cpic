#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 测试自适应阈值化方法的表现

import cv2
import numpy as np
from matplotlib import pyplot as plt

img_gray = cv2.imread('../../sources/sudoku.jpg', 0)

ret, thresh1 = cv2.threshold(img_gray, 110, 255, cv2.THRESH_BINARY)

cv2.imshow('thresh1', thresh1)
cv2.waitKey(0)
cv2.destroyAllWindows()
