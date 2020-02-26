# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 21:52:05 2019

@author: madhu
"""

import cv2
import matplotlib.pyplot as plt

img = cv2.imread('C:\\Users\\madhu\\Desktop\\Noise_salt_and_pepper.png')
median = cv2.medianBlur(img, 5)
bilateral=cv2.bilateralFilter(median,15,75,75)
display = [img, bilateral]
label = ['Original Image','Bilateral Filter applied']
fig = plt.figure(figsize=(12, 10))
for i in range(len(display)):
	fig.add_subplot(2, 2, i+1)
	plt.imshow(display[i], cmap = 'gray')
	plt.title(label[i])
plt.show()   
cv2.waitKey(0)
cv2.destroyAllWindows