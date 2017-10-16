#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import cv2
from matplotlib import pyplot as plt

img = cv2.imread('../sources/IMG_20171011_173400.jpg', 0)

plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.xticks([]), plt.yticks([]) # to hide the tick value on X and Y aixs
plt.show()

