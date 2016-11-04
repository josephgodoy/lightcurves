'''
Update: Solved the empty list problem by testing
whether or not the length of croppedTimeArray is nonzero.
If it is nonzero, the function fitting loop runs, if not,
the dataset is skipped.
Update #2: The fit parameters are now stored in an array,
fitParameters. It contains the results of each loop's popt.
'''

import matplotlib.pyplot as plt
import numpy as np
from math import floor
from scipy.optimize import curve_fit

datafile = open ('kepler.dat')
kdata = datafile.readlines()
datafile.close()

timeList = []
fluxList = []

# Populates lists with file data:

for line in kdata:
    ph = line.split()
    timeList.append(float(ph[0]))
    fluxList.append(float(ph[1]))
print("len(timeList) = ", len(timeList))

# Gaussian function definition:

def gauss (x, a, b, c):
   return a*np.exp(-(x-b)**2/(2*c**2))

# Notable constants, arrays declared here:

P = 1.76358757 #OrbitalPeriod
FirstTimeValue = timeList[0]
FirstCentroid = 0.42
fitParameters = []
z = 0

'''
# Remember: The fit parameters array stores parameters in threes.
# i, i+1, and i+2 counts as one set of popt[] values.
#
# NPeriods is exactly what it looks like. By taking the ceiling function
# of the total amount of time in the range divided by the period, you
# effectively get the number of periods in a given range. Ceiling works
# better than floor because you'd prefer an overestimate over lost data.
'''
NPeriods = int(np.ceil(((timeList[-1])-(timeList[0]))/ P))
timeArray = np.array(timeList)

# Decrements each value in timeArray by the first element's value.

timeArray = timeArray - timeArray[0]

print(timeArray[0])
fluxArray = np.array(fluxList)

for i in range(0, NPeriods):
    found = np.where((timeArray > i * P) & (timeArray < (i + 1) * P))
    croppedTimeArray = timeArray[found]
    croppedFluxArray = fluxArray[found]
    p0 = [-5, (FirstCentroid + (i * P)), 0.3]
    if len(croppedTimeArray) != 0:
        plt.plot(croppedTimeArray, croppedFluxArray, 'o')
        plt.show()
        popt, pcov = curve_fit (gauss, croppedTimeArray, croppedFluxArray, p0)
        fitParameters.append(popt[z])
        fitParameters.append(popt[z+1])
        fitParameters.append(popt[z+2])
        z = 0
        print("fit = ", popt)
        print("guess = ", p0)
        plt.plot(croppedTimeArray, gauss(croppedTimeArray, *popt))
        plt.show()
        print(fitParameters)
