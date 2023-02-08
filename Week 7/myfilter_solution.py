'''
Sample module provided for the Python Data Lab, Fall 2022.
'''
import numpy as np

def eqdistgrid(xinit,N,deltax=1):
    '''
    Create equidistant numerical grid.
    Arguments
    * xinit  : initial grid coordinate.
    * N      : total number of grid points.
    Keyword arguments
    * deltax : grid spacing.
    On return
    * grid   : equidistant numerical grid.
    '''
    grid = np.linspace(xinit,xinit+(N-1)*deltax,N)
    return grid

def boxcar(u,h=1):
    '''
    Boxcar filtering in the interior of a time series u.
    Arguments
    * u : input time series.
    Keyword arguments
    * h : filter half-width.
    On return
    * v : filtered time series.
    '''
    v = u.copy()
    #.. Implement boxcar filter using a for loop.
    for k in range(h,len(u)-h+1):
        v[k] = u[k-h:k+h+1].sum()/(2*h+1)
    return v