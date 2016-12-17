'''
======================= RESULTS.PY ============================
Results.py processes the outputs from the primary and secondary
transit-fitting methods and turns the data into useful results.
This program outputs a whitespace-delimited file with three
values:
1. The average delta-t value between eclipses.
2. The average associated uncertainty value.
3. A normalized version of the average delta-t.
It also generates and plots a histogram, as well as the
Gaussian function fit to the histogram, with associated
centroid, depth, width, and uncertainty values.
===============================================================
'''

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from scipy.optimize import curve_fit

final = open ('finaloutput.txt', 'w')
primaryFile = open ('LCP-output.txt')
secondaryFile = open ('LCS-output.txt')
primaryData = primaryFile.readlines()
secondaryData = secondaryFile.readlines()

indexA = 0
indexB = 0

# Gaussian definition:

def gauss (x, a, b, c):
   return a*np.exp(-(x-b)**2/(2*c**2))

i1 = [] # Indices for primary.py.
i2 = [] # Indices for secondary.py.
t1 = [] # Centroid times for primary.py.
t2 = [] # Centroid times for secondary.py.
u1 = [] # Uncertainty values for primary.py.
u2 = [] # Uncertainty values for secondary.py.
dt = [] # Final delta-t.
du = [] # Final uncertainty.
popt = []
pcov = []

for line in primaryData:
    pd = line.split()
    i1.append(int(pd[0]))
    t1.append(float(pd[1]))
    u1.append(float(pd[2]))

for line in secondaryData:
    sd = line.split()
    i2.append(int(sd[0]))
    t2.append(float(sd[1]))
    u2.append(float(sd[2]))

while (indexA < 806):

   #print(indexA)
   #print(u1[0], u2[0])
  # print(u1[indexA], u2[indexA])

   if u1[indexA] > 0 and u2[indexA] > 0:

      dt.append(t2[indexA] - t1[indexA])
      du.append(np.sqrt(u1[indexA] ** 2 + u2[indexA] ** 2))
      final.write("%i %f %f \n" % (indexB, dt[indexB], du[indexB]))
      indexB += 1

   indexA += 1

normalizeddt = np.array(dt) - (1.76358757 / 2.0)
avgDeltaT = sum(dt) / len(dt)
avgUncertainty = sum(du) / len(du)
avgDeltaTNormalized = (sum(dt) / len(dt)) - (1.76358757 / 2.0)

final.write ("%f | %f | %f"  % (avgDeltaT, avgUncertainty, avgDeltaTNormalized))
print ("-------------------")
print("adt, au, andt")
print("%f | %f | %f" % (avgDeltaT, avgUncertainty, avgDeltaTNormalized))
print ("-------------------")

# Histogram method:


#print(normalizeddt*1440)
#print(normalizeddt)
i = 0
n, bins, patches = plt.hist(normalizeddt*1440, 20, range=(-50, 50), facecolor = 'green')
bins2 = np.delete(bins, 20, axis = None)
bins2 = bins2 + 2.5

#for bin in (bins[0:-1]):
#    np.append(bins2, ((bins[i])+2.5))
#    i += 1

#print(bins2)
p0 = [80, 6, 10]
popt, pcov = curve_fit (gauss, bins2, n, p0, maxfev = 10000)
#popt, pcov = curve_fit (gauss, n, bins2, maxfev = 100000)
print(popt)
plt.plot(np.array(bins2), np.array(n), 'or')
plt.plot(np.array(bins2), gauss(np.array(bins2), *popt), 'r')
centroidUncertainty = np.sqrt(pcov[1,1])

print("Centroid = ", popt[1], "+/- ", centroidUncertainty)
#print(n)
#print(type(n))
##print(len(n))
#print(bins)
#print(type(bins))
#print(len(bins))
#print(bins2)
#print(len(bins2))
#print(popt)
#print(pcov)
plt.grid(True)
plt.show()
