Documentation:
_______________

  Lightcurves (lc.py) is a simple program designed for fitting inverted Gaussian functions to light curves caused by planetary and stellar bodies blocking light from brighter source bodies.

  How it works:
     Accepting whitespace-delimited files as input, Lightcurves splits data into columns
     and sorts each column into a Python list. These lists are then cropped in such a
     way that each cropped region represents one orbital period.
     Then, it fits a Gaussian function to the data, plots the data, and stores
     the fit parameters in a list. This process is repeated until the fit
     parameters for all of the sliced regions have been stored. The program then averages the
     fit parameters out, and returns an average time estimate for the center of the light curves.

  Dependencies:
  Python 3.5.2 (Anaconda custom build), NumPy, SciPy, Matplotlib (Pre-installed with Anaconda)


  Issues:
  Function fitting is still on the way.
