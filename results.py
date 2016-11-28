import numpy as np

# The big calculation:

primaryFile = open ('LCP-output.txt')
secondaryFile = open ('LCS-output.txt')
final = open ('finaloutput.txt', 'w')
primaryData = primaryFile.readlines()
secondaryData = secondaryFile.readlines()

indexA = 0
indexB = 0

i1 = [] # Indices for primary.py.
i2 = [] # Indices for secondary.py.
t1 = [] # Centroid times for primary.py.
t2 = [] # Centroid times for secondary.py.
u1 = [] # Uncertainty values for primary.py.
u2 = [] # Uncertainty values for secondary.py.
dt = [] # Final delta-t.
du = [] # Final uncertainty.

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
   if u1[indexA] > 0 and u2[indexA] > 0:
      #print(indexA) 
      dt.append(t2[indexA] - t1[indexA])
      du.append(np.sqrt(u1[indexA] ** 2 + u2[indexA] ** 2))

      final.write("%i %f %f \n" % (indexB, dt[indexB], du[indexB]))
      indexB += 1

   indexA += 1

avgDeltaT = sum(dt) / len(dt)
avgUncertainty = sum(du) / len(du)


final.write ("%f | %f"  % (avgDeltaT, avgUncertainty))
print ("-------------------")
print("%f | %f"  % (avgDeltaT, avgUncertainty))
print ("-------------------")

