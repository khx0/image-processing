#!/usr/bin/python
# -*- coding: utf-8 -*-
##########################################################################################
# author: Nikolas Schnellbaecher
# contact: khx0@posteo.net
# date: 2018-07-24
# file: extract_zstacks_wCalibration.py
# description: extract z-stacks from 5D tiff-stacks (xyczt stacking convention)
# x = x coordinate
# y = y coordinate
# c = image channel (e.g. multiple color channels)
# z = z coordinate
# t = time coordinate (for time lapse data)
# requires scikit-image
##########################################################################################
# Pixel Calibration:
# the x calibration below is provided as a resolution value in pixel / (unit of length)
# the y calibration below is provided as a resolution value in pixel / (unit of length)
# More commonly (e.g. in FIJI/ImageJ) the pixel calibration is set by the reciprocal 
# values, i.e. the pixel width (for x) is specified as value in (unit of length) / pixel
# and the pixel height (for y) is equally specified as value in (unit of length) / pixel
# For z-stacks, one also needs information about the voxel spacing. This is
# here provided using a metadata dict and the value is specified as
# value in (unit of length) / pixel.
# The metadata dict is also used to pass along a string, specifying the physical unit 
# of length for the pixel calibration.
# With these options we can set the calibration for a TIFF stack. Image processing 
# tools like FIJI will get the right values for
# * Unit of length
# * Pixel width
# * Pixel height
# * Voxel depth
# as they can be inspected by "FIJI->Image->Properties".
##########################################################################################

import sys
import time
import datetime
import os
import math
import numpy as np

import skimage
from skimage import io
from skimage.external import tifffile
from skimage.external.tifffile import TiffFile
from skimage.external.tifffile import TiffWriter

def ensure_dir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)

now = datetime.datetime.now()
now = "%s-%s-%s" %(now.year, str(now.month).zfill(2), str(now.day).zfill(2))

BASEDIR = os.path.dirname(os.path.abspath(__file__))
RAWDIR = os.path.join(BASEDIR, 'data')
OUTDIR = os.path.join(BASEDIR, 'zstacks')
 
if __name__ == '__main__':
    
    ######################################################################################
    # user settings
        
    filename = 'input-5D-stack.tif'
    
    framename = 'zstack_frame_t_'
    
    print "loading ...", filename
    
    ensure_dir(os.path.join(BASEDIR, OUTDIR))
    
    ######################################################################################
    # set x-y resolution
    # The x and y resolution is provided in (numerator, denominator) 
    # in px per unit of measure.
    # E.g. a tuple of
    # x_resolution = (4, 5)
    # with a unit measure in micron = um = 1e-6 meter
    # means, that the calibration factor is given as
    # 4/5 = 0.8 px/um.
    # The inverse of this value, i.e.
    # 5/4 um / px is often more commonly referred to as the pixel width (for x) 
    # and the pixel height for (y).
    # This information can e.g. be extracted using the TiffFile.info() function.
    x_resolution = (2585297, 1000000)
    y_resolution = (2585297, 1000000)
    
    xResFactor = float(x_resolution[0]) / float(x_resolution[1])
    yResFactor = float(y_resolution[0]) / float(y_resolution[1])

    resolution = (xResFactor, yResFactor)

    # set up metadata
    metadata = {'spacing': 2.5,\
                'unit': 'micron',\
                'axes': 'TZCXY'}
    
    ######################################################################################
    
    with TiffFile(os.path.join(RAWDIR, filename)) as tif:
        
        data = tif.asarray() # extract raw numpy array
        
        print data.shape
        
        # ensure that the 5D stacking convention is valid and change if needed
        nFrames = data.shape[0]
	
        print "nFrames =", nFrames
        
        for i in range(nFrames):
            
            outname = os.path.join(OUTDIR, framename + str(i + 1).zfill(3) + '.tif')
            
            zstack = data[i]
            
            print i, zstack.shape, "writing to ->", outname

            # the imsave command uses the stack order
            # that is passed in the metadata dict
            zstack.shape = 1, zstack.shape[0], 1, zstack.shape[1], zstack.shape[2]
            
            tifffile.imsave(outname, zstack, 
			                imagej = True,
			                resolution = resolution,
			                metadata = metadata)





            

		
		
		
		
		
		