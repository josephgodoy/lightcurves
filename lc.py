import matplotlib.pyplot as plt
import numpy as np
from math import floor
from scipy.optimize import curve_fit

datafile = open ('kepler.dat')
kdata = datafile.readlines()
datafile.close()

timeList = []
fluxList = []

for line in kdata:
    ph = line.split()
    timeList.append(float(ph[0]))
    fluxList.append(float(ph[1]))

print(len(timeList))

def gauss (x, a, b, c):
   return a*np.exp(-(x-b)**2/(2*c**2))

OrbitalPeriod = 1.76358757
FirstTimeValue = 169.53073
NumOfTimeValues = 1519915
ReducedTimeValues = 1519914
poptResults = []
NLoops = 0

#Solution 1: List comprehension. (?)
#while (NLoops < (ReducedTimeValues/OrbitalPeriod)):
#    croppedList = [timeList for x in range (TimeArray[(FirstTimeValue + (N * OrbitalPeriod) < FirstTimeValue + (N+1) * OrbitalPeriod)])]

#Solution 2: List comprehension II. (?)
#while (NLoops < (ReducedTimeValues/OrbitalPeriod)):
#    croppedList = [timeList for x in range (TimeArray[(FirstTimeValue + (N * OrbitalPeriod), (FirstTimeValue + (N+1) * OrbitalPeriod))])]

#Solution 3: NumPy array magic. (?)
#M = FirstTimeValue + OrbitalPeriod
#croppedList = timeList[ OrbitalPeriod <= timeList ]
#croppedList = croppedList[ croppedList < M ]
