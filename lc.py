'''
   lc.py - version 4:

   Updates:
      -New cropping method, tested multiple times, fully functional.

   Next Steps:
      -Loop Gaussian function over each cropped set of timeList[] values.
      -Update Gaussian guess parameters.
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
poptResults = []
croppedTimeList = []
croppedFluxList = []
NLoops = 0
i = 0

'''
# This is working! It starts at [0] and stops when [2548] exceeds the condition.
# All that's left to do is get rid of the previous interval.
'''

while True and i <= ReducedTimeValues:
   for index in timeList:
       if timeList[i] > (FirstTimeValue + (NLoops * OrbitalPeriod) + OrbitalPeriod):
           print("Condition met at entry [%d]." % i)
           NLoops += 1
           break
       else:
           croppedTimeList.append(timeList[i])
           croppedFluxList.append(fluxList[i])
           i += 1
   croppedTimeArray = np.array(croppedTimeList)
   croppedFluxArray = np.array(croppedFluxList)
   plt.plot(croppedTimeList, croppedFluxList, 'o')
   plt.show()
   while croppedTimeList:
      croppedTimeList.pop() 
   while croppedFluxList:
      croppedFluxList.pop()
    

