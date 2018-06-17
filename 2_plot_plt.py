# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 21:24:04 2017

@author: Sriram
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('watch.jpg',cv2.IMREAD_GRAYSCALE)

plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.plot([100,210,210,100,100],[20,20,120,120,20],'c', linewidth=5)
plt.show()