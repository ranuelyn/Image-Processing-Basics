# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 22:04:47 2023

@author: yusuf
"""

import cv2
import matplotlib.pyplot as plt

# import the image
img = cv2.imread('img1.JPG')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.figure()
plt.imshow(img, cmap = 'gray')
plt.axis('off')
plt.show() 

# making the threshold
_, thresh_img = cv2.threshold(img, thresh = 60, maxval = 255, type = cv2.THRESH_BINARY) # thresh_binary make white the ones out of the boundry
plt.figure()
plt.imshow(thresh_img, cmap = 'gray')
plt.axis('off')
plt.show() 

# adaptive threshold

thresh_img2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 8)
plt.figure()
plt.imshow(thresh_img2, cmap = 'gray')
plt.axis('off')
plt.show() 