# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 00:00:10 2018

@author: Sriram
"""
import numpy as np
import cv2
img = cv2.imread('bookpage.jpg')

ret, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)
grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret2, threshold2 = cv2.threshold(grayscaled, 12, 255, cv2.THRESH_BINARY)
gaus = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
ret3, threshold3 = cv2.threshold(grayscaled,125,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow('Original', img)
cv2.imshow('Threshold', threshold)
cv2.imshow('Threshold2', threshold2)
cv2.imshow('Gauss', gaus)
cv2.imshow('OTSU', threshold3)
cv2.waitKey(0)
cv2.destroyAllWindows()