'''
   lc.py - version 5:

   Updates:
      -Cropping method is working, gaussian function call added.
      -Added comments for clarification.
   Next Steps:
      -Refine Gaussian guess parameters.
      -Compute running average (averageDelta) instead of using a sample list.
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

OrbitalPeriod = 1.76358757
FirstTimeValue = 169.530573
NumOfTimeValues = 1519915
ReducedTimeValues = 1519914
FirstCentroid = 169.947427
NLoops = 0
i = 0
averageDelta = 1.763
poptResults = []
croppedTimeList = []
croppedFluxList = []

'''
This segment loops over all of the items in the list of time values,
appending each value in timeList[] to a new croppedTimeList[],
until a value outside of the crop interval of size OrbitalPeriod is reached.
Then, the values are converted into NumPy arrays, fitted and plotted, and the
loop starts back over again, repeating the process.
'''

while True and i <= ReducedTimeValues:
   for index in timeList:
       #This loop crops an interval of size OrbitalPeriod.
       if timeList[i] > (FirstTimeValue + (NLoops * OrbitalPeriod) + OrbitalPeriod):
           print("Condition met at entry [%d]." % i)
           NLoops += 1
           break
       else:
           #Iteratively populates cropped lists with time, flux list values.
           croppedTimeList.append(timeList[i])
           croppedFluxList.append(fluxList[i])
           i += 1
   croppedTimeArray = np.array(croppedTimeList)
   croppedFluxArray = np.array(croppedFluxList)
   #fittedData = gauss(croppedTimeArray, 10, (NLoops * FirstCentroid), 5)
   # p0 = (?, ?, ?)
   # p0 = (10, (169.948 + (averageDelta * NLoops)), 5)
   # popt, pcov = curve_fit (gauss, croppedTimeArray, croppedFluxArray, p0)
   # plt.plot(croppedTimeList, fittedFluxList)
   plt.plot(croppedTimeArray, croppedFluxArray, 'o')
   plt.show()
   # This empties out the lists, making room for
   # the next set of values.
   while croppedTimeList:
      croppedTimeList.pop()
   while croppedFluxList:
      croppedFluxList.pop()
