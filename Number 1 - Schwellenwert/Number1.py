#!/usr/bin/env python

# Trackbars for colors 
# Better style and functionality than Trackbars1.py

import numpy as np
import cv2
from matplotlib import pyplot as plt


def TBChanged(x):
    tresh = cv2.getTrackbarPos('tresh', 'image')

    _,result = cv2.threshold(img,tresh,255,cv2.THRESH_BINARY)
    cv2.imshow('result', result)

# Load Image and transform to Grey
img = cv2.imread('seeds.tif')
grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Create 
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.moveWindow('image', 20, 30)
cv2.namedWindow('result', cv2.WINDOW_NORMAL)
cv2.moveWindow('result', 450, 30)

# create trackbars for color change
cv2.createTrackbar('tresh', 'image', 0, 255, TBChanged)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()