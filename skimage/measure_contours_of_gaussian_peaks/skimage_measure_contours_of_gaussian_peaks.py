#!/usr/bin/python
# -*- coding: utf-8 -*-
##########################################################################################
# author: Nikolas Schnellbaecher
# contact: nikolas.schnellbaecher@bioquant.uni-heidelberg.de
# date: 2018-08-27
# file: skimage_measure_contours_of_gaussian_peaks.py
# requires: scikit-image
# https://scikit-image.org/
# Tested with Python 3.7.0, matplotlib 2.2.2, skimage 0.14.0
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
    
def create_2D_Gaussian_data(mu, cov, nVisPoints = 100):
    
    # create 2D Gaussian peak
    x, y = np.meshgrid(np.linspace(-3.0, 3.0, nVisPoints), 
                       np.linspace(-3.0, 3.0, nVisPoints))
                       
    z = np.zeros((nVisPoints, nVisPoints))
    
    # fill z array
    for i in range(nVisPoints):
        
        for j in range(nVisPoints):
        
            p = np.zeros((2,))
            p[0], p[1] = x[0, i], y[j, 0]
            
            z[i, j] = multivariateNormal(p, mu, cov)
    
    return z
    
if __name__ == '__main__':

    outname = 'skimage_measure_contours_of_gaussian_peaks'

    # Example A
    # set mean (vector) and covariance (matrix)
    mu = np.zeros((2,))
    cov = np.zeros((2, 2))
    cov[0, 0] = 1.0
    cov[1, 1] = 1.0
    
    zA = create_2D_Gaussian_data(mu, cov)
    
    # measure the contour
    contourlevel = 0.1
    contoursA = measure.find_contours(zA, contourlevel)    
    
    # Example B
    # set mean (vector) and covariance (matrix)
    mu = np.zeros((2,))
    cov = np.zeros((2, 2))
    cov[0, 0] = 1.0
    cov[0, 1] = 3.0 / 5.0
    cov[1, 0] = 3.0 / 5.0
    cov[1, 1] = 2.0
    
    zB = create_2D_Gaussian_data(mu, cov)
    
    # measure the contour
    contourlevel = 0.1
    contoursB = measure.find_contours(zB, contourlevel)    
    
    # Example C
    # set mean (vector) and covariance (matrix)
    mu = np.zeros((2,))
    cov = np.zeros((2, 2))
    cov[0, 0] = 4.0
    cov[0, 1] = -3.0
    cov[1, 0] = -3.0
    cov[1, 1] = 5.0
    
    zC = create_2D_Gaussian_data(mu, cov)
    
    # measure the contour
    contourlevel = 0.03
    contoursC = measure.find_contours(zC, contourlevel)   
    
    ######################################################################################
    # show results using matplotlib's pyplot
    fig, ax = plt.subplots(1, 3)
    
    ax[0].imshow(zA, interpolation = 'nearest', cmap = plt.cm.gray)
    ax[1].imshow(zB, interpolation = 'nearest', cmap = plt.cm.gray)
    ax[2].imshow(zC, interpolation = 'nearest', cmap = plt.cm.gray)
    
    for i, contour in enumerate(contoursA):
        ax[0].plot(contour[:, 1], contour[:, 0], linewidth = 2.0)
        
    for i, contour in enumerate(contoursB):
        ax[1].plot(contour[:, 1], contour[:, 0], linewidth = 2.0)    
        
    for i, contour in enumerate(contoursC):
        ax[2].plot(contour[:, 1], contour[:, 0], linewidth = 2.0)   
    
    fig.savefig(os.path.join(OUTDIR, outname) + '.pdf', dpi = 300, transparent = True)
    
    plt.show()
    
    
    