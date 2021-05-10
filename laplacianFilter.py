# -*- coding: utf-8 -*-
"""
Created on Mon May 3 18:58:45 2021

@author: Narcís
"""

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import scipy.signal as ss

img = (cv.imread(r'C:\...POSA AQUI LA TEVA ROOT...\.jpg',1))
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

lap = np.array([[0,-1,0], #creem un laplacià
                [-1,4,-1],
                [0,-1,0]])

plt.figure(dpi=300) 
plt.imshow(img, CMAP='gray')

img2 = np.abs(ss.convolve2d(img,lap,mode='same')) #convolució amb laplacià
img2[0:371,0]=img2[0:371,534]=img2[0,0:534]=img2[371,0:534]=0
img2 = np.round(img2*255/(np.amax(img2)-np.amin(img2)),0)

plt.figure(dpi=300)
plt.imshow(img2, CMAP='gray')
