# -*- coding: utf-8 -*-
"""
Created on Mon May 3 18:24:01 2021

@author: Narcís
"""


import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

#carrega imatge
img = (cv.imread(r'C:\...POSA AQUI LA TEVA ROOT....jpg',1))
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

plt.figure(dpi=300)
plt.imshow(img, CMAP='gray')

for a in range(0,img.shape[0]): #creem un soroll random a la imatge
    for b in range(0,img.shape[1]):
        d = np.random.uniform(0,1)*100
        if d>=99:
            img[a,b] =0
        elif d<=1:
            img[a,b] = 255

plt.figure(dpi=300) #imatge sorollosa
plt.imshow(img,cmap='gray')

img_filter = cv.medianBlur(img,3) #filtratge per medianas 3x3

plt.figure(dpi=300)
plt.imshow(img_filter,cmap='gray')

img_filter = cv.medianBlur(img,9) #filtratge per medianas 9x9

plt.figure(dpi=300)
plt.imshow(img_filter,cmap='gray')