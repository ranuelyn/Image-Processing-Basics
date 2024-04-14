# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 22:24:28 2023

@author: yusuf
"""

import cv2
import matplotlib.pyplot as plt
import numpy as np
import warnings
warnings.filterwarnings('ignore')

# import the image
img = cv2.imread('NYC.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.figure()
plt.imshow(img)
plt.title('NYC Original')
plt.axis('off')
plt.show()

# blurring (blurring)

dst2 = cv2.blur(img, ksize = (3,3))
plt.figure()
plt.imshow(dst2)
plt.title('NYC Blurred')
plt.axis('off')
plt.show()

# gaussian blur
gb = cv2.GaussianBlur(img, ksize = (3,3), sigmaX = 7)
plt.figure()
plt.imshow(gb)
plt.title('NYC Gaussian Blurred')
plt.axis('off')
plt.show()

# median blur
mb = cv2.medianBlur(img, ksize = (3, 3))
plt.figure()
plt.imshow(mb)
plt.title('NYC Median Blur')
plt.axis('off')
plt.show()

def gaussianNoise(image):
    row, col, ch = image.shape
    mean = 0
    var = 0.05
    sigma = var ** 0.5
    
    gauss = np.random.normal(mean, sigma, (row, col, ch))
    gauss = gauss.reshape(row, col, ch)
    noisy = image + gauss
    
    return noisy

# import and normalize it
img = cv2.imread('NYC.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) / 255 # normalize
plt.figure()
plt.imshow(img)
plt.title('NYC Original')
plt.axis('off')
plt.show()

gaussianNoiseImage = gaussianNoise(img)
plt.figure()
plt.imshow(gaussianNoiseImage)
plt.title('Gaussian Blurred Image')
plt.axis('off')
plt.show()

# gaussian blur
gb2 = cv2.GaussianBlur(gaussianNoiseImage, ksize = (3,3), sigmaX = 7)
plt.figure()
plt.imshow(gb2)
plt.title('NYC -noisy- Gaussian Blurred')
plt.axis('off')
plt.show()

#%% pepper and salt noise

def saltPepperNoise(image):
    row,col,ch = image.shape
    s_vs_p = 0.5
    amount = 0.004
    noisy = np.copy(image)
    # Salt mode
    num_salt = np.ceil(amount * image.size * s_vs_p)
    coords = [np.random.randint(0, i - 1, int(num_salt)) for i in image.shape]
    noisy[coords] = 1

    # Pepper mode
    num_pepper = np.ceil(amount* image.size * (1. - s_vs_p))
    coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in image.shape]
    noisy[coords] = 0
  
    return noisy


spImage = saltPepperNoise(img)
plt.figure()
hor = np.hstack((img, spImage))
plt.imshow(hor)
plt.title('NYC \nOriginal & Salt-Peppered Image')
plt.axis('off')
plt.show()

























