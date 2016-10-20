Documentation: 
_______________

  Lightcurves is a simple program designed for fitting inverted Gaussian functions to 
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

  Note: Not all of these features are fully working at the moment.