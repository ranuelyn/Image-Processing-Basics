# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 00:44:39 2023

@author: yusuf
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('red_blue.jpg')
img_vis = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.figure()
plt.imshow(img_vis)
plt.axis('off')
plt.title('Red-Blue Image')

print(img.shape)
# 407358

img_hist = cv2.calcHist([img], channels = [0], mask = None, histSize = [256], ranges = [0,256]) 
print(img_hist.shape)
plt.figure()
plt.plot(img_hist)

color = ('b', 'g', 'r')
plt.figure()

for i, c in enumerate(color):
    hist = cv2.calcHist([img], channels = [i], mask = None, histSize = [256], ranges = [0,256]) 
    plt.plot(hist, color = c)
    
golden_gate = cv2.imread('goldenGate.jpg')
golden_gate_vis = cv2.cvtColor(golden_gate, cv2.COLOR_BGR2RGB)
plt.figure()
plt.imshow(golden_gate)

print(golden_gate.shape)
#23970816

mask = np.zeros(golden_gate.shape[:2], np.uint8)
plt.figure()
plt.imshow(mask, cmap = 'gray')

mask[1500:2000, 1000:2000] = 255
plt.figure()
plt.imshow(mask, cmap = 'gray')

maskedImg2 = cv2.bitwise_and(golden_gate_vis, golden_gate_vis, mask = mask)
plt.figure()
plt.imshow(maskedImg2, cmap = 'gray')

masked_img = cv2.bitwise_and(golden_gate, golden_gate, mask = mask)
masked_img_hist = cv2.calcHist([golden_gate], channels = [0], mask = mask, histSize = [256], ranges = [0,256]) # color channel order bgr bu nedenle channel sıfır yazıyoruz.
plt.figure()
plt.plot(masked_img_hist)

# make the histograms same
# increase the contrast

img = cv2.imread('hist_equ.jpg', 0)
plt.figure()
plt.imshow(img, cmap = 'gray')

img_hist = cv2.calcHist([img], channels = [0], mask = None, histSize = [256], ranges = [0,256])
plt.figure()
plt.plot(img_hist)

eq_hist = cv2.equalizeHist(img)
plt.figure()
plt.imshow(eq_hist, cmap = 'gray')

eq_img_hist = cv2.calcHist([eq_hist], channels = [0], mask = None, histSize = [256], ranges = [0,256])
plt.figure()
plt.plot(eq_img_hist)


