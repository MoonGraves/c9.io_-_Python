import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

# sampling frequency in Herz
Fs = 44100              #näytteenottotaajuus

# IIR filter coefficients a0, a1, a2,....1, b1, b2, b3, ...

a, b = signal.iirfilter(3, Wn=0.05, rp=1, rs=40, btype='lowpass', ftype='butter')
w, h = signal.freqz(a, b)

# (w/2*np.pi) = digital frequency, digitaalinen taajuus.
# Digital frequency for a signal equels 1 when the real signal frequency equals to Fs sampling frequency. 
# Signaalin digitaalinen taajuus = 1, kun signaalin taajuus on yhtä suuri kuin näytteenottotaajuus. 

# The freguency f for the signal in Herz, signaalin taajuus f yksikkönä Herzi.
f = (w/(2*np.pi))*Fs

# Transfer function   -  Siirtofunktio  tai Systeemifunktio 
Coeff = str(a)+ "/" + str(b)    # represented here as ascii string for printing on plot. 

#plt.title('Digital filter frequency response')
plt.title(Coeff)
#Amplitude Responce in decibels for signal level = 20 log (Output/Input)
plt.plot(f, 20*np.log10(np.abs(h)))
plt.ylabel('Amplitude Response [dB]')
plt.xlabel('Frequency [Hz]')
plt.grid()
plt.show()