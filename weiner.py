from scipy import ndimage
from scipy import signal
from matplotlib import pyplot as plt
import cv2
import numpy as np
from scipy import misc
face = misc.face(gray=True)
face = face[:512, -512:] 
face=cv2.imread('C:\\Users\\madhu\\Desktop\\speckle.PNG')
noisy_face = np.copy(face).astype(np.float)
noisy_face += face.std() * 0.5 * np.random.standard_normal(face.shape)
wiener_face = signal.wiener(noisy_face, (5, 5))
plt.imshow(wiener_face, cmap=plt.cm.gray)
plt.title('Wiener filter')