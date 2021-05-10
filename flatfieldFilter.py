# -*- coding: utf-8 -*-
"""
Created on Mon May 3 19:41:25 2021

@author: Narcís
"""

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt


img = (cv.imread(r'C:\...POSA AQUI LA TEVA ROOT....\jpg',1))
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

x = np.abs(np.linspace(0,img.shape[0]-1,img.shape[0]))
y = (np.linspace(0,img.shape[1]-1,img.shape[1]))
sig = img.shape[0]*3
gaussian = np.zeros((img.shape))
for a in range(0,img.shape[0],1): #simulació de vinyetatge a través d'una gaussiana amb una sigma molt gran
    for b in range(0,img.shape[1],1):
        gaussian[a,b] = np.exp(-(a-img.shape[0]/2)**2/(0.5*sig**2))*np.exp(-(b-img.shape[1]/2)**2/(0.5*sig**2))
        
plt.figure(dpi=300)
plt.imshow(gaussian,cmap='gray') #imatge gaussiana

plt.figure(dpi=300)
plt.imshow(img,cmap='gray') #imatge UOC

img_vinyetatge = img*gaussian

plt.figure(dpi=300)
plt.imshow(img_vinyetatge,cmap='gray') #imatge amb vinyetatge

img_filtered = img_vinyetatge/gaussian

plt.figure(dpi=300)
plt.imshow(img_filtered,cmap='gray') #imatge filtrada

#òbviament aquí estem multiplicant per els mateixos valors perquè és una simulació,
#però en realitat tíndriem una imatge de calibració que aplicariem a la imatge
# per obtenir la correcció de flat field
