# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 22:22:58 2018

@author: Sriram
"""
import cv2
import numpy as np
cap = cv2.VideoCapture('E:/DATASCIENCEGO’S DISCUSSION PANEL ON CAREERS.mp4')
 
while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
 
    cv2.imshow('frame',frame)
    #cv2.imshow('gray',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()