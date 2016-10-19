'''
 lc.py - version 3:

 Updates:
    -Documentation improved.
    -Fixed a faulty constant.

  Next Steps:
    -Fix cropping.
    -Loop Gaussian function over each cropped set of timeList[] values.

  Other Notes:
    -As one might expect, the first and last values on a given OrbitalPeriod
     are not necessarily sampled in kepler.dat.
    -Possible solution: 
      + Check indexed values until one escapes the acceptable range.
      + Store the index and use it as the first entry in the next loop, rinse, repeat.
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

# Populates lists with their respective data points:

for line in kdata:
    ph = line.split()
    timeList.append(float(ph[0]))
    fluxList.append(float(ph[1]))
print(len(timeList))

# Gaussian function:

def gauss (x, a, b, c):
   return a*np.exp(-(x-b)**2/(2*c**2))

# Notable constants, arrays declared here:
# NOTE: All previous versions of lc are using an incorrect value
# for FirstTimeValue (timeList[0]).
# The correct value is, in fact, 169.530573.

OrbitalPeriod = 1.76358757
FirstTimeValue = 169.530573
NumOfTimeValues = 1519915
ReducedTimeValues = 1519914
poptResults = []
NLoops = 0
n = 0

# Think of this like a 'reverse array' method:
# Input a desired value, get a list index.

print("Find index for value:")
wantedValue = input()
while True:
    if timeList[n] == wantedValue:
       print("%d") % n
       break
   elif timeList[n] != wantedValue:
       n += 1

# Potential Solution 1: List comprehension. (?)
# while (NLoops < (ReducedTimeValues/OrbitalPeriod)):
#    croppedList = [timeList for x in range (TimeArray[(FirstTimeValue + (N * OrbitalPeriod) < FirstTimeValue + (N+1) * OrbitalPeriod)])]

# Potential Solution 2: List comprehension II. (?)
# while (NLoops < (ReducedTimeValues/OrbitalPeriod)):
#    croppedList = [timeList for x in range (TimeArray[(FirstTimeValue + (N * OrbitalPeriod), (FirstTimeValue + (N+1) * OrbitalPeriod))])]

# Potential Solution 3: NumPy array magic. (?)
# M = FirstTimeValue + OrbitalPeriod
# croppedList = timeList[ OrbitalPeriod <= timeList ]
# croppedList = croppedList[ croppedList < M ]
