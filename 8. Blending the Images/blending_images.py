# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 17:40:46 2023

@author: yusuf
"""

import cv2
import matplotlib.pyplot as plt

# blending
# the default import point is that the colors are reading as BGR
# so we need to convert it as an RGB color with cvtColor
img1 = cv2.imread('img1.JPG')
img1 = cv2.cvtColor(img1, cv2.COLl_BGR2RGB)
img2 = cv2.imread('img2.JPG')
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)


plt.figure()
plt.imshow(img1)

plt.figure()
plt.imshow(img2)

print(img1.shape)
print(img2.shape)

img1 = cv2.resize(img1, (600, 600))
print(img1.shape)
img2 = cv2.resize(img2, (600, 600))
print(img2.shape)

plt.figure()
plt.imshow(img1)

plt.figure()
plt.imshow(img2)

# blended image = a * img1 + beta * img2
blendedImg = cv2.addWeighted(src1 = img1, alpha = 0.5, src2 = img2, beta = 0.5, gamma = 0)
plt.figure()
plt.imshow(blendedImg)