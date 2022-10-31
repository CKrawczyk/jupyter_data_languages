# Jupyter notebooks for PhD class on data languages.

## Installing python
The easiest way to install python on any OS is to use [anaconda python](https://www.continuum.io/downloads).  This will install a local version of python on your system so you don't need to worry about needing admin to install new packages.  Most of the packages listed above are installed by default with anaconda.  For this class we will be using python 3, and I recommend you use this version for you research.

## Packages to install (in addition to anaconda's defaults)
+ `pymc`
+ `graphviz`
+ `reproject`

```bash
pip install pymc graphviz reproject 
```

## Class 1
- `Git.ipynb`: Git and Git-Hub
- `General_Python.ipynb`: General python information
- `Unit_testing.ipynb`: Writing unit tests in python

## Class 2
- `General_plotting.ipynb`: How to make publication ready plots
- `mpl_style.py`: How to make a `matplotlib` style
- `Uncertainty_plotting.ipynb`: Making plots with errorbars
- `Stats_with_Scipy.ipynb`: using `scipy` for stats distributions

## Class 3
- `Astropy_fitting.ipynb`: using `astropy` to model and fit data
- `mcmc_fit_with_outliers_pymc.ipynb`: fitting a line to data while rejecting outliers using MCMC (pymc3)
- `Gaussian_proces_theory.ipynb`: introduction to GPs
- `Gaussian_process_regression_pymc.ipynb`: fitting data without defining a functional form
