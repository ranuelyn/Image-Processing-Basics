# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 16:46:59 2023

@author: yusuf
"""

import cv2

# resized

img = cv2.imread('lenna.png')
print('Image Size: ', img.shape)
cv2.imshow('Original', img)

imgResized = cv2.resize(img, (800, 800))
print('Resized Img Shape', imgResized.shape)
cv2.imshow('Resized', imgResized)

# crop

imgCropped = img[:300, 0:300] # height -> width
cv2.imshow('Cropped', imgCropped)