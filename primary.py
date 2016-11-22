'''
================= PRIMARY.PY ===============================
Latest update: Primary output is now written to a whitespace-delimited
file of the following three-column format:
Orbit Number | Centroid Location | Uncertainty.
Slices with no data in them will have values of -99.
Slices with unreliable data (uncertainty > 1) will have values of -98.
============================================================
'''

import matplotlib.pyplot as plt
import numpy as np
from math import floor
from scipy.optimize import curve_fit

#I/O preparation:

datafile = open ('kepler.dat')
output = open('LCP-output.txt', 'w')
kdata = datafile.readlines()
datafile.close()
timeList = []
fluxList = []

# Populates lists:

for line in kdata:
    ph = line.split()
    timeList.append(float(ph[0]))
    fluxList.append(float(ph[1]))

# Gaussian function definition:

def gauss (x, a, b, c):
   return a*np.exp(-(x-b)**2/(2*c**2))

# Notable constants and arrays:

P = 1.76358757 # Orbital period in days.
FirstTimeValue = timeList[0]
FirstCentroid = 0.42
w = 0.3   # Width of cropping region. Do NOT use in the Gaussian.
eclipseTime = 1.3
fitParameters = []
NPeriods = int(np.ceil(((timeList[-1])-(timeList[0]))/ P))
timeArray = np.array(timeList)
fluxArray = np.array(fluxList)
timeArray = timeArray - timeArray[0]

# The magic happens here:

for i in range(0, NPeriods):

    found = np.where((timeArray > i * P) & (timeArray < (i + 1) * P))
    croppedTimeArray = timeArray[found]
    croppedFluxArray = fluxArray[found]
    p0 = [-5, (FirstCentroid + (i * P)), 0.3] # Depth-centroid-width p0 array.
    print(croppedTimeArray)

    if len(croppedTimeArray) != 0:

        print("i = %i" % i)

        plt.plot(croppedTimeArray, croppedFluxArray, 'o')
        popt, pcov = curve_fit (gauss, croppedTimeArray, croppedFluxArray, p0, maxfev = 100000)
        fitParameters.append(popt[0])
        fitParameters.append(popt[1])
        fitParameters.append(popt[2])

        print("Centroid = ", popt[1], "+/- ", np.sqrt(pcov[1,1]))
        print("Guess = ", p0)

        if np.sqrt(pcov[1,1]) > 1:
           output.write("%i %f %f \n" % (i, -98, -98))
        else:
           output.write("%i %f %f \n" % (i, popt[1], np.sqrt(pcov[1,1])))

        plt.plot(croppedTimeArray, gauss(croppedTimeArray, *popt))
        #plt.show()

    elif len(croppedTimeArray) == 0:
        output.write("%i %f %f \n" % (i, -99, -99))

print(fitParameters)
output.close()
