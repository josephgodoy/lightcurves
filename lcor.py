import matplotlib.pyplot as plt
import numpy as np
from math import floor
from scipy.optimize import curve_fit
"""
Version 5: Update Notes:
    -Note: The np.clip() function doesn't operate how I thought it did.
	-Instead of cropping the array/list, it truncates values.
	-Attempting a list slice in the while-loop. (5:7)
"""
datafile = open ('kepler.dat')
kdata = datafile.readlines()
datafile.close()

timeList = []
fluxList = []

for line in kdata:
    p = line.split()
    timeList.append(float(p[0]))
    fluxList.append(float(p[1]))

def gauss (x, a, b, c):
   return a*np.exp(-(x-b)**2/(2*c**2))

OrbitalPeriod = 1.76358757
FirstTimeValue = 169.53073
indexA = 0
indexB = FirstTimeValue
N = 0
poptResults = []
while indexA < 10:
   timeArray = np.array(timeList)
   fluxArray = np.array(fluxList)
   #list slicing!
   while FirstTimeValue + (N * OrbitalPeriod) < FirstTimeValue + (N+1) * OrbitalPeriod:
      # note: np.clip does NOT do what you want it to.
      arg1 = (FirstTimeValue + N * OrbitalPeriod)
      arg2 = (FirstTimeValue + (N+1) * OrbitalPeriod)
      timeList2 = timeList[arg1:arg2]
      #(timeArray, (FirstTimeValue + (N * OrbitalPeriod)): (FirstTimeValue + (N + 1) * OrbitalPeriod))
      croppedTimeArray = np.array(timeList2)
      #NEED: Update guess parameters with each instance.
      #First, we have to find reasonables guesses for a single light curve.
      #Then, we have to set up a variable linked to those guesses that increments
      #with each completion of the for-loop.
      #y = gauss(timeArray, #guess1, #guess2, #guess3)
      #Updates the 'centroid' value of p0 with each iteration of the loop.
      #p0 = [2, (FirstTimeValue + (N + 0.5) * OrbitalPeriod) , .1]
      #popt, pcov = curve_fit (gauss, timeArray, fluxArray, p0)
      #poptResults.append(popt)
      #plt.plot(timeArray, gauss(fluxArray, *popt))
      plt.plot(timeList2, fluxArray)
      plt.show()
   indexA += 1
   N += 1
   '''indexC = FirstTimeValue * (N+1) ? '''
#while indexC <= len(poptResults[])
#print(poptResults[indexC])
