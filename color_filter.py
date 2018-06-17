# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 22:42:13 2018

@author: Sriram
"""
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _,frame = cap.read()
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    width = cap.get(3)
    height = cap.get(4)
    lower_red = np.array([50,150,50])
    upper_red = np.array([200,255,255])

    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame, frame, mask=mask)
    
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    
    k =cv2.waitKey(5) & 0xFF
    if k==27:
        break
    
cv2.destroyAllWindows()
cap.release()

print(height,width)