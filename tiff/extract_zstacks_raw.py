#!/usr/bin/python
# -*- coding: utf-8 -*-
##########################################################################################
# author: Nikolas Schnellbaecher
# contact: khx0@posteo.net
# date: 2018-07-24
# file: extract_zstacks_raw.py
# raw refers to only extracting the pixel matrices and dropping potentially relevant
# meta data for pixel calibration
# description: extract z-stacks from 5D tiff-stacks (xyczt stacking convention)
# x = x coordinate
# y = y coordinate
# c = image channel (e.g. multiple color channels)
# z = z coordinate
# t = time coordinate (for time lapse data)
# requires scikit-image
##########################################################################################

import sys
import time
import datetime
import os
import math
import numpy as np

import skimage
from skimage import io

def ensure_dir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)

now = datetime.datetime.now()
now = "%s-%s-%s" %(now.year, str(now.month).zfill(2), str(now.day).zfill(2))

BASEDIR = os.path.dirname(os.path.abspath(__file__))
RAWDIR = os.path.join(BASEDIR, 'data')
OUTDIR = os.path.join(BASEDIR, 'zstacks_raw')
 
ZERO_PADDING = 3 

if __name__ == '__main__':

    ######################################################################################
    # user settings
    
    filename = 'input-5D-stack.tif'
    
    framename = 'zstack_frame_t_'
    
    print "loading ...", filename
    
    ensure_dir(OUTDIR)
    
    ######################################################################################
    
    im = io.imread(os.path.join(RAWDIR, filename))
    
    print im.shape
    
    # ensure that the 5D stacking convention is valid and change if needed
    nFrames = im.shape[0]
    
    print "nFrames =", nFrames
    
    for i in range(nFrames):
    
        outname = os.path.join(OUTDIR, \
                               framename + str(i + 1).zfill(ZERO_PADDING) + '.tif')
	    
	    zstack = im[i]
	    
	    print i, zstack.shape
	    
	    # this saves each z-stack as a raw pixel matrix
	    # meta data from the original 5-D stack is most likely lost
	    io.imsave(outname, zstack)
	    
	    
	    