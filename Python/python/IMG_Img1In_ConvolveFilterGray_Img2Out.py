"""
Filter for gray scale images. In plotting out the image the colour mapping 
plt.cm.gray scales the calculated values into range 0 ... 255 . There is 
no risk on overflowing the 8 bit gray value. 
Timo Karppinen  2.4.2017
"""

import matplotlib.pyplot as plt
import numpy as np
import imageio

from scipy import ndimage   # ndimage for n-dimensional images
                            # https://docs.scipy.org/doc/scipy-0.18.1/reference/ndimage.html
#tossa on rivissä 10 import imageio, jonka pitää ladata
# python.exe -m pip install imageio

#img1=ndimage.imread('c:/temp/Image/Brittiautot_png_comp9_600x400_tkar2008.png', flatten=True, mode=None )
#ndimage.grey_opening('c:/temp/Image/Brittiau   tot_png_comp9_600x400_tkar2008.png', size=None, footprint=None  )

#oman tämä scipy versio on 1.4.1, how check scipy versio: avaa visual studio coden alhaalta:: cmd / powershell / Python debug console
#cmd ja powershell ovat sama, Windows-käyttöjärjestelmän komentotulkki
 
# scipy version tarkistus & huom siinä on kaksi alaviivaa:::
# >>>import scipy
# >>>scipy.__version__
#'1.4.1'

#huom!!! lukee tiedoston kansion, älä käytä \ merkkiä, joka menee omatietokone pollun mukaan, osa koodi kielessä menee / mukaan
#lyhyin tapa hakee kuvan tiedosto './(kuvan_nimi).npg'
img1 = imageio.imread('./chevrolet_models.jpg', as_gray=True, pilmode=None)

#matriisi (matrix - mathematic)
H = np.array([[0,0,0,0,0],
             [0,-1,-2,-1,0],
             [0,0,0,0,0],
             [0,-1,-2,-1,0],
             [0,0,0,0,0]])

'''
([[1,1,0,-1,-1],
             [1,1,0,-1,-1],
             [1,1,1,-1,-1],
             [1,1,0,-1, -1],
             [1,1,0,-1,-1]])

             ([[0,1,2,1,0],              
            [1,2,3,2,1],              
            [2,3,3,3,2],              
            [1,2,3,2,1],              
            [0,1,2,1,0]]) 
'''
#mode tyyppit: constant, nearest, full, reflect,
#mode='constant', cval=0
#mode='nearest'
img2 = ndimage.convolve(img1, H, mode='nearest', cval=0, origin=0)

#värin sanastot, mitkä tulee tohon riville --> cmap=plt.cm.(värinnimi) esim. cmap=plt.cm.spring & cmap=plt.cm.RdBu
#https://matplotlib.org/3.1.1/tutorials/colors/colormaps.html
#figsize = kuva koko (leveys, korkeus)

fig = plt.figure(figsize=(11, 3))
plt.subplot(121)
plt.imshow(img1, cmap=plt.cm.gray)
plt.title('Unfiltered gray scale image')

plt.subplot(122)
plt.imshow(img2, cmap=plt.cm.gist_gray)
plt.title('Filtered with convolution matrix H')
plt.show()