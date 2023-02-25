"""
Filter for colour images. Please be careful with your coeffiecients in matrix H.
The sum of filter coefficients must be jst less than 1.
There is nothing to limit the pixel colour channel  value to overflow the 8 bit value.
255 = 1111 1111 ,  256 = 1 0000 0000 and you will get colour corresponding 0000 0000 .
Timo Karppinen  17.12.2018
"""

import matplotlib.pyplot as plt
import numpy as np
import imageio

from scipy import ndimage   # ndimage for n-dimensional images
                            # https://docs.scipy.org/doc/scipy-0.18.1/reference/ndimage.html


#img1=ndimage.imread('c:/temp/Image/Brittiautot_png_comp9_600x400_tkar2008.png', flatten=False, mode=None )
img1 = imageio.imread('./race_car.png', as_gray=False, pilmode=None)

shape1 = img1.shape         # shape1 = (400,600,4)
height = shape1[0]          # shape1[0] = 400
width = shape1[1]           # shape1[1] = 600
bitsPerPixel = shape1[2]     # shape1[2] = 4 

"""
H = np.array([[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],
              [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],
              [[0,0,0,0],[0,0,0,0],[0,0,1,0],[0,0,0,0],[0,0,0,0]],
              [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],
              [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]])
"""            
#shapeH = H.shape
#rows = shapeH[0]
#columns = shapeH[1]
#colourBytes = shapeH[2]

#img2 = ndimage.convolve(img1, H, mode='reflect', cval=0, origin=0)

#img3 = ndimage.imread('C:/Users/zhao-/Desktop/python/race_car.png', flatten=False, mode=None )   
img3 = imageio.imread('./race_car.png', as_gray=False, pilmode=None)

# defines that img3 is of type "image"

for i in range(0,height):
   for j in range(0,width):
        #img3[i,j,0] = 255  # for testing the variable type try with value 0, 32, 245, 254, 255, 256, 265, -10
        img3[i,j,0] = (0.7*img1[i,j,0] + 0.0*img1[i,j,1] + 0.0*img1[i,j,2]) + 50 # red channel
        img3[i,j,1] = (0.0*img1[i,j,0] + 0.7*img1[i,j,1] + 0.0*img1[i,j,2]) + 20 # green channel
        img3[i,j,2] = (0.0*img1[i,j,0] + 0.0*img1[i,j,1] + 0.7*img1[i,j,2]) + 0 # blue channel
        #img3[i,j,3] = img2[i,j,3] # transparency channel 50 misty, 255 non transparent

for i in range(0,height):
   for j in range(0,width):
       if img3[i,j,0] < 0:
            img3[i,j,0] = 0
       if img3[i,j,1] < 0:
            img3[i,j,0] = 0
       if img3[i,j,2] < 0:
            img3[i,j,0] = 0
       if img3[i,j,0] > 254:
            img3[i,j,0] = 255
       if img3[i,j,1] > 254:
            img3[i,j,0] = 255
       if img3[i,j,2] > 254:
            img3[i,j,0] = 255


fig = plt.figure(figsize=(18, 6))
plt.subplot(131)
plt.imshow(img1)
plt.title('Unfiltered image of size '+str(width)+'*'+str(height)+' with '+str(bitsPerPixel)+' byte colour' )

#plt.subplot(132)
#plt.imshow(img2)
#plt.title('Filtered with convolution matrix H of dimension '+str(rows)+' by '+str(columns)+' by '+str(colourBytes))

plt.subplot(133)
plt.imshow(img3)
plt.title('Channels colour values manipulated for each pixel')
plt.show()