LightCurves
================

LightCurves is a simple set of programs and scripts designed to find relativistic Romer delay times in on-edge, transiting planetary systems. The program fits inverted Gaussian functions to primary and secondary transit curves, locating their centroids, and comparing
  the time differences between them. 

### Dependencies:

Python 3.5.X (Anaconda custom build), NumPy, SciPy, Matplotlib

### Usage:

After installing all requisite packages, run this script from the command line:

   bash lightcurves.sh

This script will run primary.py, secondary.py, and results.py, in that order.
As of right now, this set of programs works only with the kepler.dat dataset. 
`
