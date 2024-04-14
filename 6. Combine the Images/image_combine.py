# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 17:25:06 2023

@author: yusuf
"""

import cv2
import numpy as np

# import the image
img = cv2.imread('lenna.png')
cv2.imshow('Original', img)

# horizontal 
hor = np.hstack((img, img))
cv2.imshow('HorizontalStack', hor)

# vertical
ver = np.vstack((img, img))
cv2.imshow('VerticalStack', ver)
