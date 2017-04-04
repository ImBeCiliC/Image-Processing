#!/usr/bin/env python

# Trackbars for colors 
# Better style and functionality than Trackbars1.py

import numpy as np
import cv2

def TBChanged(x):
    r = cv2.getTrackbarPos('R', 'image')
    g = cv2.getTrackbarPos('G', 'image')
    b = cv2.getTrackbarPos('B', 'image')
    s = cv2.getTrackbarPos(switch, 'image')

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b,g,r]

    cv2.imshow('image', img)

# Create an empty (black) image
img = np.zeros((300, 512, 3), np.uint8)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.moveWindow('image', 10, 30)

# create trackbars for color change
cv2.createTrackbar('R', 'image', 0, 255, TBChanged)
cv2.createTrackbar('G', 'image', 0, 255, TBChanged)
cv2.createTrackbar('B', 'image', 0, 255, TBChanged)

# create switch 
switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch, 'image', 0, 1, TBChanged)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()