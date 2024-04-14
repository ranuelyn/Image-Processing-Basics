# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 16:12:36 2023

@author: yusuf
"""

import cv2

#%% içe aktarma

img = cv2.imread('messi5.jpg', 0)

#%% görselleştir

cv2.imshow(('first image'), img)
k = cv2.waitKey(0) &0xFF

if k == 27: #wsc
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('messi_gray.png', img)
    cv2.destroyAllWindows()