# Jupyter notebooks for PhD class on data languages.

## Installing python
The easiest way to install python on any OS is to use [anaconda python](https://www.continuum.io/downloads).  This will install a local version of python on your system so you don't need to worry about needing admin to install new packages.  Most of the packages listed above are installed by default with anaconda.  For this class we will be using python 3, and I recommend you use this version for you research.

## Packages to install (in addition to anaconda's defaults)
+ `emcee`
+ `reproject`

```bash
pip install emcee reproject
```

## Class 1
- `Git.ipynb`: Git and Git-Hub
- `General_Python.ipynb`: General python information
- `Unit_testing.ipynb`: Writing unit tests in python

## Class 2
- `General_plotting.ipynb`: How to make publication ready plots
- `mpl_style.py`: How to make a `matplotlib` style
- `Uncertainty_plotting.ipynb`: Making plots with errorbars
- `Fits_images.ipynb`: Plotting image contained in FITS files

## Class 3
- `Stats_with_Scipy.ipynb`: using `scipy` for stats distributions
- `Astropy_fitting.ipynb`: using `astropy` to model and fit data
- `mcmc_fit_with_outliers.ipynb`: fitting a line to data while rejecting outliers using MCMC
- `Gaussian_process_regression`: fitting data without defining a functional form
