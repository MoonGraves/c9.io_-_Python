"""
IIR digital filter 
x    signal input
y    signal output
H    transfer function

H(z) =[ a0 + a1(z^-1) + a2(z^-2) + a3(z^-3) ] / [ 1 + b1(z^-1) + b2(z^-2) + b3(z^-3) ]

z^-1 delay of one sampling period
z^-2 delay of two sampling periods
...

Fs   sampling frequency
T    sampling period

f    signal frequency
Timo Karppinen, 30.3.2017
"""

import numpy as np
import matplotlib.pyplot as plt


Fs = 44100      # sampling frequency 44100 Hz is used for example in audio CD.
T  = 1/Fs

f = 40000        # Please start with value 1500 Hz then try 62Hz, 125Hz, 250Hz, 500Hz, 1000Hz, 2000Hz, 4000Hz, 8000Hz
                # Please write down the output signal amplitude on each frequency

n = np.linspace(0, 4095, 4095)          # number of samples in the plot np.linspace(0, 4095, 4096)

x = 0.5*np.sin(2*np.pi*f*n*T)

y = [0]*len(x)                  # Array for y values. Same length as array for x values

# As an example a second order bandpass IIR filter with pass band from 500Hz to 3000Hz, Fs 44100Hz
# Coefficients were calculated with online filter design tool at http://engineerjs.com/
"""
a0 = 0.02518
a1 = 0
a2 = -0.05035
a3 = 0
a4 = 0.02518
b1 = -3.45
b2 = 4.517
b3 = -2.671
b4 = 0.6044
"""
a = [0.01682, 0, -0.03364, 0, 0.01682]

b = [1, -3.491, 4.674, -2.848, 0.6684]


for n in range(4, len(x-4)):
    y[n] = a[0]*x[n] + a[1]*x[n-1] + a[2]*x[n-2] + a[3]*x[n-3] + a[4]*x[n-4] - b[1]*y[n-1] - b[2]*y[n-2] - b[3]*y[n-3] - b[4]*y[n-4]


fig = plt.figure(figsize=(18, 6))

plt.subplot(211)
plt.plot( x,'b-', linewidth=2)
plt.xlabel( 'sample length' )
plt.ylabel( 'Input signal' )
plt.grid()

plt.subplot(212)
plt.plot( y,'r-', linewidth=2)
plt.xlabel( 'sample length' )
plt.ylabel( 'Output signal' )
plt.grid()
plt.show()