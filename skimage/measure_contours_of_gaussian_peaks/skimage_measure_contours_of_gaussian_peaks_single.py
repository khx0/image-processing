#!/usr/bin/python
# -*- coding: utf-8 -*-
##########################################################################################
# author: Nikolas Schnellbaecher
# contact: nikolas.schnellbaecher@bioquant.uni-heidelberg.de
# date: 2018-08-27
# file: skimage_measure_contours_of_gaussian_peaks_single.py
# requires: scikit-image
# https://scikit-image.org/
##########################################################################################

import sys
import time
import datetime
import os
import math
import numpy as np
import matplotlib.pyplot as plt

from skimage import measure

def ensure_dir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)

now = datetime.datetime.now()
now = "%s-%s-%s" %(now.year, str(now.month).zfill(2), str(now.day).zfill(2))

BASEDIR = os.path.dirname(os.path.abspath(__file__))
RAWDIR = os.path.join(BASEDIR, 'raw')
OUTDIR = os.path.join(BASEDIR, 'out')

ensure_dir(OUTDIR)
ensure_dir(RAWDIR)

def multivariateNormal(x, mu, cov):
    v = x - mu
    invCov = np.linalg.inv(cov)
    exponent = np.matmul(invCov, v)
    exponent = np.matmul(v.T, exponent)
    prefactor = 1.0 / np.sqrt(np.linalg.det(2.0 * np.pi * cov))
    return prefactor * np.exp(-exponent / 2.0)

if __name__ == '__main__':

    outname = 'skimage_measure_contours_of_a_gaussian_peak'
    
    ######################################################################################
    # create 2D Gaussian peak
    
    nVisPoints = 100
    
    # set mean (vector) and covariance (matrix)
    mu = np.zeros((2,))
    cov = np.zeros((2, 2))
    cov[0, 0] = 1.0
    cov[1, 1] = 1.0
    
    print("mu.shape =", mu.shape)
    print("cov.shape =", cov.shape)
    
    x, y = np.meshgrid(np.linspace(-3.0, 3.0, nVisPoints), 
                       np.linspace(-3.0, 3.0, nVisPoints))
        
    z = np.zeros((nVisPoints, nVisPoints))
    
    for i in range(nVisPoints):
        
        for j in range(nVisPoints):
        
            p = np.zeros((2,))
            p[0], p[1] = x[0, i], y[j, 0]
            
            z[i, j] = multivariateNormal(p, mu, cov)
    
    print("z.shape =", z.shape)
    print(np.max(z), np.min(z))
    
    # save data to file
    np.savetxt(os.path.join(RAWDIR, 'gaussian_peak_data.txt'), z, fmt = '%.8f')  
    
    
    ######################################################################################
    # find contours at a constant value specified by the
    # contourlevel variable
    contourlevel = 0.1
    
    # returns a list, that contains all detected contours
    contours = measure.find_contours(z, contourlevel)
    
    print("Number of contours found: ", len(contours))
    for i, contour in enumerate(contours):
        print(i, "contour.shape =", contour.shape)
    ######################################################################################
    
    ######################################################################################
    # show results using pyplot
    fig, ax = plt.subplots()
    
    ax.imshow(z, interpolation = 'nearest', cmap = plt.cm.gray)
    
    for i, contour in enumerate(contours):
        ax.plot(contour[:, 1], contour[:, 0], linewidth = 2.0)
    
    fig.savefig(os.path.join(OUTDIR, outname) + '.pdf', dpi = 300, transparent = True)
    
    plt.show()

    

    
    
    
    