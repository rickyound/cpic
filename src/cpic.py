#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import cv2
import numpy as np
from matplotlib import pyplot as plt

img_ori = cv2.imread('../sources/img_little.jpg')

img = cv2.cvtColor(img_ori, cv2.COLOR_BGR2RGB)

rows, cols, ch = img.shape
# rows=388, cols=520, ch=3

# 重点在于这几个点如何获取
pts1 = np.float32([[72, 10], [483, 10], [0, rows], [cols, rows]])
pts2 = np.float32([[0, 0], [cols, 0], [0, rows], [cols, rows]])

M = cv2.getPerspectiveTransform(pts1, pts2)

dst = cv2.warpPerspective(img, M, (cols, rows))

cv2.imwrite('../targets/img_little.jpg', img_ori)
cv2.imwrite('../targets/img_little_dst.jpg', cv2.cvtColor(dst, cv2.COLOR_RGB2BGR))

plt.subplot(121), plt.imshow(img), plt.title('Input'), plt.xticks([]), plt.yticks([])
plt.subplot(122), plt.imshow(dst), plt.title('Output'), plt.xticks([]), plt.yticks([])
plt.show()
