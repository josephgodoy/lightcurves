Documentation: 
_______________

  Lightcurves (lc.py) is a simple program designed for fitting inverted Gaussian functions to 
  primary and secondary light curves (transits) caused by planetary and stellar bodies
  blocking light from a brighter source body. 
  
  How it works:
     Accepting a whitespace-delimited file as input, lc.py splits the data into columns
     and sorts each column into a Python list. These lists are then cropped in such a 
     way that each crop represents one orbital period's worth of data points. 
     Then, it proceeds to fit a Gaussian function to the data, plot the data, and store
     the fit parameters in another list. This process is rinsed and repeated until the fit 
     parameters for all of the slices have been stored. The program then averages these 
     fit parameters out, and returns the average location of an eclipse.

  Dependencies:
  Python 3.5.2 (Anaconda custom build), NumPy, SciPy, Matplotlib (Pre-installed with Anaconda)
     
  
  Issues: 
  Function fitting is still on the way. (Plotting and cropping work perfectly, though!)
