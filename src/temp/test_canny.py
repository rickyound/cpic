#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ≤‚ ‘ÕºœÒCanny±ﬂ‘µºÏ≤‚

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('../../sources/img_little.jpg', 0)

edges = cv2.Canny(img, 80, 200)

plt.subplot(121), plt.imshow(img, cmap='gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(edges, cmap='gray')
plt.title('Edges Image'), plt.xticks([]), plt.yticks([])

plt.show()
