#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 在同一个目录内的图片幻灯片展示
# 利用cv2.addWeighted方法实现平滑过渡

# author by rick
# 2017-10-18

# 备注@20171018，暂未完美实现

import numpy as np
import cv2
import time
import os

names = os.listdir('../sources')

def load_two_images(num):
    if len(names) < 2:
        return cv2.imread('../sources/' + names[0], 1), None
    if num == 0:
        return cv2.imread('../sources/' + names[0], 1), cv2.imread('../sources/' + names[1], 1)
    return cv2.imread('../sources/' + names[num - 1], 1), cv2.imread('../sources/' + names[num], 1)

cv2.namedWindow('image', cv2.WINDOW_NORMAL)

for x in xrange(1, len(names)):
    cur_img, nxt_img = load_two_images(x)

    cur_img_rows, cur_img_cols, cur_img_channels = cur_img.shape
    nxt_img_rows, nxt_img_cols, nxt_img_channels = nxt_img.shape

    print 'cur_img: %s %s %s' % (cur_img_rows, cur_img_cols, cur_img_channels)
    print 'nxt_img: %s %s %s' % (nxt_img_rows, nxt_img_cols, nxt_img_channels)

    min_rows = cur_img_rows if cur_img_rows <= nxt_img_rows else nxt_img_rows
    min_cols = cur_img_cols if cur_img_cols <= nxt_img_cols else nxt_img_cols

    print min_rows, min_cols

    cur_ori = cur_img[0:min_rows, 0:min_cols]
    nxt_ori = nxt_img[0:min_rows, 0:min_cols]

    #cv2.imshow('cur', cur_ori)
    #cv2.imshow('nxt', nxt_ori)
    
    cv2.imshow('image', cur_img)
    if (cv2.waitKey(0) & 0xFF == ord('n')):
        ind = 0
        inc = 1
        while(1):
            img = cv2.addWeighted(cur_ori, 0.1*(10-ind), nxt_ori, 0.1*ind, 0)
            cur_img[0:min_rows, 0:min_cols] = img
            cv2.imshow('image', cur_img)
            time.sleep(0.3)
            if ind == 10:
                break
            ind = ind + inc

cv2.destroyAllWindows()
