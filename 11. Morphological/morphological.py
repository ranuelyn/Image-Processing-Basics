# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 23:15:02 2023

@author: yusuf
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

#%% import the image

img = cv2.imread('datai_team.jpg', 0)
plt.figure()
plt.imshow(img, cmap = 'gray')
plt.axis('off')
plt.title('Original Image')

# erosion

kernel = np.ones((5,5), dtype = np.uint8)
result = cv2.erode(img, kernel, iterations= 1)
plt.figure()
plt.imshow(result , cmap = 'gray')
plt.axis('off')
plt.title('Erosion Image')

# dilation
result2 = cv2.dilate(img, kernel, iterations = 1)
plt.figure()
plt.imshow(result2 , cmap = 'gray')
plt.axis('off')
plt.title('Dilation Image')

#%% white noice

whiteNoice = np.random.randint(0, 2, size = img.shape[:2])
whiteNoice = whiteNoice * 255
plt.figure()
plt.imshow(whiteNoice , cmap = 'gray')
plt.axis('off')
plt.title('White Noice Image')

wNoisyImg = whiteNoice + img
plt.figure()
plt.imshow(wNoisyImg , cmap = 'gray')
plt.axis('off')
plt.title('White Noiced Image')

# reduce the noice with opening
opening = cv2.morphologyEx(wNoisyImg.astype(np.float32), cv2.MORPH_OPEN, kernel)
plt.figure()
plt.imshow(opening , cmap = 'gray')
plt.axis('off')
plt.title('Opening Image')

# black noice

blackNoice = np.random.randint(0, 2, size = img.shape[:2])
blackNoice = blackNoice * -255
bNoicyImg = blackNoice + img
bNoicyImg[bNoicyImg <= -245] = 0
plt.figure()
plt.imshow(bNoicyImg , cmap = 'gray')
plt.axis('off')
plt.title('Black Noiced Image')

# reduce the black noice with closing

closing = cv2.morphologyEx(bNoicyImg.astype(np.float32), cv2.MORPH_CLOSE, kernel)
plt.figure()
plt.imshow(closing , cmap = 'gray')
plt.axis('off')
plt.title('Closed Image')

# morphological gradient -> to detect the edges of the target

gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
plt.figure()
plt.imshow(gradient , cmap = 'gray')
plt.axis('off')
plt.title('Gradient Image')
























