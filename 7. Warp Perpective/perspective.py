# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 17:30:14 2023

@author: yusuf
"""

import cv2
import numpy as np

# import the image

img = cv2.imread('card.png')
cv2.imshow('Original', img)

width = 400
height = 500


pts1 = np.float32([[204, 2], [1, 474], [541, 150], [339, 618]])
pts2 = np.float32([[0,0], [0, height], [width, 0], [width, height]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)
print(matrix)

# final image warped
warpedImg = cv2.warpPerspective(img, matrix, (width, height))
cv2.imshow('Final Image', warpedImg)
