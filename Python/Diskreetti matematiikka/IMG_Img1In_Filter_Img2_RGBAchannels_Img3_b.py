import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage  # ndimage for n-dimensional images
import imageio

                            # https://docs.scipy.org/doc/scipy-0.18.1/reference/ndimage.html


img1 = imageio.imread('./race_car.png', as_gray=False, pilmode=None )

shape1 = img1.shape         # shape1 = (400,600,4)
height = shape1[0]          # shape1[0] = 400
width = shape1[1]           # shape1[1] = 600
bitsPerPixel = shape1[2]     # shape1[2] = 4 

#H = np.array([[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],
               #[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],
               #[[0,0,0,0],[0,0,0,0],[0,0,1,0],[0,0,0,0],[0,0,0,0]],
               #[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],
              #[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]])
              
#shapeH = H.shape
#rows = shapeH[0]
#columns = shapeH[1]
#colourBytes = shapeH[2]             

#img2 = ndimage.convolve(img1, H, mode='reflect', cval=0, origin=0)

img3 = imageio.imread('./race_car.png', as_gray=False, pilmode=None )   
# defines that img3 is of type "image"

for i in range(0,height):
   for j in range(0,width):
        img3[i,j,0] = 255  # for testing the variable type try with value 0, 32, 245, 254, 255, 256, 265, -10
        img3[i,j,0] = (0.5690*img1[i,j,0] + 0.0*img1[i,j,1] + 0.0*img1[i,j,2]) + 49 # red channel
        img3[i,j,1] = (0.0*img1[i,j,0] + 0.5870*img1[i,j,1] + 0.0*img1[i,j,2]) + 45 # green channel
        img3[i,j,2] = (0.0*img1[i,j,0] + 0.0*img1[i,j,1] + 0.5760*img1[i,j,2]) + 50 # blue channel
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


fig = plt.figure(figsize=(15, 4))
plt.subplot(131)
plt.imshow(img1)
plt.title('Unfiltered image of size '+str(width)+'*'+str(height)+' with '+str(bitsPerPixel)+' byte colour' )

#plt.subplot(132)
#plt.imshow(img1)
#plt.title('Filtered with convolution matrix H of dimension '+str(rows)+' by '+str(columns)+' by '+str(colourBytes))

plt.subplot(133)
plt.imshow(img3)
plt.title('Channels colour values manipulated for each pixel')
plt.show()