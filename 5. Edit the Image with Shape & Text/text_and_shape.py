# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 17:10:12 2023

@author: yusuf
"""

import cv2
import numpy as np

# create an image
img = np.zeros((512,512,3), np.uint8) # a black image
print(img.shape)

cv2.imshow('BlackImage', img)

# create a line
# image, starting point, ending point, color, thickness
cv2.line(img, (0, 0), (512, 512), (0,255,0), 3) # BGR = (X,X,X)
cv2.imshow('Line', img)

# create a rectangle
# image, starting point, ending point, color, filled or not
cv2.rectangle(img, (0,0), (256, 256), (82,11,31), cv2.FILLED)
cv2.imshow('Rectangle', img)

# create a circle
# image, mid point, radius, color, filled or not
cv2.circle(img, (256,256), 45, (0,0,255), cv2.FILLED)
cv2.imshow('Circle', img)

# create a text
# image, starting point, font, thickness, color
cv2.putText(img, 'Image', (256, 256), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255))
cv2.imshow('Text', img)
