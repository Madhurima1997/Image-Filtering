# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 01:53:03 2019

@author: madhu
"""
#C:\\Users\\madhu\\Documents\\books n notes\\vit sem1\\set1\\lenagauss.PNG
#C:\\Users\\madhu\\Documents\\books n notes\\vit sem1\\set1\\lenapoisson.PNG
#C:\\Users\\madhu\\Documents\\books n notes\\vit sem1\\set1\\lenasaltpep.PNG
#C:\\Users\\madhu\\Documents\\books n notes\\vit sem1\\set1\\lenaspeckle.PNG
import cv2
import numpy as np
import math
from matplotlib import pyplot as plt

def psnr(img1, img2):
    mse=np.mean((img1-img2)**2)
    if mse==0:
        return 100
    PIXEL_MAX=255.0
    return 20*math.log10(PIXEL_MAX/math.sqrt(mse))

def mse(imageA, imageB):
	# the 'Mean Squared Error' between the two images is the
	# sum of the squared difference between the two images;
	# NOTE: the two images must have the same dimension
	err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
	err /= float(imageA.shape[0] * imageA.shape[1])
	
	# return the MSE, the lower the error, the more "similar"
	# the two images are
	return err

if __name__ == '__main__':
    img = cv2.imread('C:\\Users\\madhu\\Documents\\books n notes\\vit sem1\\set1\\lenaspeckle.PNG')
    
    blur = cv2.blur(img,(5,5))

    plt.subplot(121),plt.imshow(img),plt.title('Noisy Image')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(blur),plt.title('After Mean Filter')
    plt.xticks([]), plt.yticks([])
    plt.show()
    m=mse(img, blur)
    print(m)
    d = psnr(img, blur)
    print(d)    