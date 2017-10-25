#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import cv2
import numpy as np
from matplotlib import pyplot as plt

img_ori = cv2.imread('../sources/img_little.jpg')

img = cv2.cvtColor(img_ori, cv2.COLOR_BGR2RGB)

rows, cols, ch = img.shape

# 重点在于这几个点如何获取
pts1 = np.float32([[69, 30], [473, 30], [4, 354], [500, 354]])
pts2 = np.float32([[0, 0], [496, 0], [0, 324], [496, 324]])

M = cv2.getPerspectiveTransform(pts1, pts2)

dst = cv2.warpPerspective(img, M, (496, 324))

plt.subplot(121), plt.imshow(img), plt.title('Input'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(dst), plt.title('Output'), plt.xticks([]), plt.yticks([])
plt.show()
