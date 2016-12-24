LightCurves
================

LightCurves is a simple set of programs and scripts designed to calculate Romer delay times in on-edge, transiting planetary systems. The program fits inverted Gaussian functions to primary and secondary transit curves, locating their centroids, and comparing
  the time differences between them. 

### Dependencies:

Python 3.5.X (Anaconda custom build), NumPy, SciPy, Matplotlib

### Usage:

After installing all requisite packages, run this script from the command line:

>bash lightcurves.sh

This script will run primary.py, secondary.py, and results.py, in that order.

After the three programs have completed their tasks, a histogram of the various offsets will be displayed, as well as a Gaussian fit to the histogram, approximating the value of the Romer delay (or, in elliptical orbits, the sum of the eccentricity-related delay plus the Romer delay).

### Notes:

As of 12/24/16, this set of programs works only with a dataset from the Kepler Space Telescope, kepler.dat. Work has started on generalizing the programs for other datasets, targets, and purposes.
