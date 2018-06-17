# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 22:13:49 2018

@author: Sriram
"""
import numpy as np
import cv2
img1 = cv2.imread('3D-Matplotlib.png')
img2 = cv2.imread('mainsvmimage.png')
img3 = cv2.imread('mainlogo.png')

#add = img1 + img2
#add = cv2.add(img1,img2)
#weighted = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)
rows,cols,channels = img3.shape
roi = img1[0:rows, 0:cols]
img2gray = cv2.cvtColor(img3 , cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)
#cv2.imshow('mask', mask)
mask_inv = cv2.bitwise_not(mask)
#cv2.imshow('inv',mask_inv)
img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
#cv2.imshow('bg',img1_bg)
img3_fg = cv2.bitwise_and(img3, img3, mask=mask)
#cv2.imshow('fg',img3_fg)
dst = cv2.add(img1_bg,img3_fg)
img1[0:rows,0:cols] = dst
cv2.imshow('res', img1)

cv2.waitKey(0)
cv2.destroyAllWindows()