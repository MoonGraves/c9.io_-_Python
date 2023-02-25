"""
FIR suodin
x   signal in  esimerkiksi siniaalto sopivalla taajuudella
y   signal out suotimen laskema suodatettu lähtevä signaali
H   transfer function  Muodostuu termeistä h0, h1, h2, h3, ...hN
N   N point filter   Suotimen siirtofunktion termien määrä
n   number of samples    Tarkastelussa mukana olevien näytteiden määrä

z^-1  delay one sampling period   Yhden näytteenottovälin mittainen viive
z^-2  delay two sampling periods

Fs  Sampling frequency  Näytteenottotaajuus
T   Sampling period     Näytteenottoaikaväli

f   Signal frequency    Käsiteltävän signaalin taajuus
"""

import numpy as np
import matplotlib.pyplot as plt

Fs = 44100          # CD quality audio
T = 1/ Fs

n = np.linspace(0, 1023, 1024)   # array starting 0 last value 1023 altogether 1024

f = 1500            # input signal frequency

x = 0.5*np.sin(2*np.pi*f*n*T)  # input signal as array 

y = [0]*len(x)
"""
# Filter coefficients. For example from Timo's DSP fundamentals...
h0 = 0.0
h1 = 0.0468
h2 = 0.1009
h3 = 0.1514
h4 = 0.1872
h5 = 0.2
h6 = 0.1872
h7 = 0.1514
h8 = 0.1009
h9 = 0.0468
h10= 0.0
"""
h =[
    0.028606809032122517,
-0.023417140450215198,
0.010223855274120303,
-0.04646552100142527,
-0.05061272344496961,
-0.0008095517505120781,
0.017856361687544106,
0.0015739066837766328,
-0.0045303777230935255,
0.002904668742555286,
0.0037941107496921844,
0.001056324827672498,
0.002840101556738353,
-0.00036916267304454845,
-0.015371394348349762,
-0.027775400832234363,
-0.018722382751612795,
0.011708169243101017,
0.04335941514934658,
0.051407576012586845,
0.02351163541333385,
-0.028577462704707488,
-0.0713006861406304,
-0.070796444709691,
-0.020233037898044814,
0.05063908200377051,
0.09383640072260733,
0.07700484677873295,
0.007854303307333611,
-0.06907473718490138,
0.8977752188277287,
-0.06907473718490138,
0.007854303307333611,
0.07700484677873295,
0.09383640072260733,
0.05063908200377051,
-0.020233037898044814,
-0.070796444709691,
-0.0713006861406304,
-0.028577462704707488,
0.02351163541333385,
0.051407576012586845,
0.04335941514934658,
0.011708169243101017,
-0.018722382751612795,
-0.027775400832234363,
-0.015371394348349762,
-0.00036916267304454845,
0.002840101556738353,
0.001056324827672498,
0.0037941107496921844,
0.002904668742555286,
-0.0045303777230935255,
0.0015739066837766328,
0.017856361687544106,
-0.0008095517505120781,
-0.05061272344496961,
-0.04646552100142527,
0.010223855274120303,
-0.023417140450215198,
0.028606809032122517
]

"""
for n in range(10, len(x)):
    y[n] = h0*x[n] + h1*x[n-1] + h2*x[n-2] + h3*x[n-3] + h4*x[n-4] + h5*x[n-5] + h6*x[n-6] + h7*x[n-7] + h8*x[n-8] + h9*x[n-9] + h10*x[n-10]
""" 
for n in range(len(x)):
    for i in range(len(h)):
        y[n] = y[n] + h[i]*x[n-i]


plt.subplot(211)
plt.plot( x, 'b-', linewidth=2)
plt.xlabel('sample number')
plt.ylabel('Input signal')
plt.grid()

plt.subplot(212)
plt.plot( y, 'r-', linewidth=2)
plt.xlabel('sample number')
plt.ylabel('Output signal')
plt.grid()

plt.show()