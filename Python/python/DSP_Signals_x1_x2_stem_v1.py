import matplotlib.pyplot as plt 
import numpy as np 
 
f = 3800            # signal frequency f = 1000 Hz 
T = 0.000125        # sampling frequency 8000 Hz, sampling period T = 0.000125 seconds  

n = np.linspace(0, 63, 64) # number of samples in the plot np.linspace(0, 63, 64)
x1 = 1*np.sin(2*np.pi*f*n*T)
#x2 = 1*np.sin(2*np.pi*f*n*T)+1
 
fig = plt.figure() 
plt1 = fig.add_subplot(211)      # two rows, one column, subplot one 
#plt2 = fig.add_sudbplot(212)      # two rows, one column, subplot two 
 
markerline, stemlines, baseline1 = plt1.stem(n, x1, '-.') # presentation of sampled values 
#markerline, stemlines, baseline2 = plt2.stem(n, x2, '-.') 
 
plt.setp(baseline1, 'color', 'b', 'linewidth', 2) 
#plt.setp(baseline2, 'color', 'r', 'linewidth', 2) 

plt.xlabel('X-label')
plt.ylabel('Y-label')

plt.show() 