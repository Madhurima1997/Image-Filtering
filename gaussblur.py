# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 19:54:23 2019

@author: madhu
"""

import cv2
import numpy 

img = cv2.imread('C:\\Users\\madhu\\Desktop\\220px-Halftone,_Gaussian_Blur.jpg')
median = cv2.GaussianBlur(img,(5,5),cv2.BORDER_DEFAULT)
cv2.imshow("Gaussian Smoothing",numpy.hstack((img, median)))
cv2.waitKey(0)
cv2.destroyAllWindows