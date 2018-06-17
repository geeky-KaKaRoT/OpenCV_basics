# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 21:22:36 2017

@author: Sriram
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt
#image=cv2.imread('watch.jpg')
img = cv2.imread('watch.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()