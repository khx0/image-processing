#!/usr/bin/python
# -*- coding: utf-8 -*-
##########################################################################################
# author: Nikolas Schnellbaecher
# contact: khx0@posteo.net
# date: 2018-07-24
# file: save_stack_with-xy-resolution.py
##########################################################################################

import sys
import time
import datetime
import os
import math
import numpy as np

import skimage
from skimage import io
from skimage.external.tifffile import TiffFile
from skimage.external.tifffile import TiffWriter

def ensure_dir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)

now = datetime.datetime.now()
now = "%s-%s-%s" %(now.year, str(now.month).zfill(2), str(now.day).zfill(2))

BASEDIR = os.path.dirname(os.path.abspath(__file__))
RAWDIR = os.path.join(BASEDIR, 'data')
OUTDIR = os.path.join(BASEDIR, 'out')

ZERO_PADDING = 3

if __name__ == '__main__':
    
    ######################################################################################
    # user settings
        
    filename = 'myTifImageFile.tif'
    
    framename = 'frame_t_'
    
    print "loading ...", filename
    
    ensure_dir(os.path.join(OUTDIR))
        
    ######################################################################################
    # set x-y resolution
    # The x and y resolution is provided in (numerator, denominator) 
    # in px per unit of measure. This is a way to specify rational numbers by a tuple
    # of integer variables.
    # E.g. a tuple of
    # x_resolution = (4, 5)
    # with a unit measure in micron = um = 1e-6 meter
    # means, that the calibration factor is given as
    # 4/5 = 0.8 px/um.
    # The inverse of this value, i.e.
    # 5/4 um / px is often more commonly referred to as the pixel width (for x) 
    # and the pixel height for (y).
    x_resolution = (2585297, 1000000)
    y_resolution = (2585297, 1000000)
    ######################################################################################
    resolution = (x_resolution, y_resolution, None)
    # the resolution argument has the syntax
    # resolution : (float, float[, str]) or ((int, int), (int, int)[, str])
    ######################################################################################
    
    with TiffFile(os.path.join(RAWDIR, filename)) as tif:
        
        data = tif.asarray()
        
        print data.shape
        
        nFrames = data.shape[0]
    
        print "nFrames =", nFrames
        
        for i in range(nFrames):
            
            outname = os.path.join(OUTDIR, framename + str(i + 1).zfill(ZERO_PADDING) + '.tif')
            
            image = data[i]
            
            print i, image.shape, "writing to ->", outname
            
            with TiffWriter(outname) as tifw:
                
                tifw.save(image, 
			              resolution = resolution)
		
		
		
		
		
		
		