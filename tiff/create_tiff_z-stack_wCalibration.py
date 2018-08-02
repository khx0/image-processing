#!/usr/bin/python
# -*- coding: utf-8 -*-
##########################################################################################
# author: Nikolas Schnellbaecher
# contact: khx0@posteo.net
# date: 2018-08-01
# file: create_tiff_z-stack_wCalibration.py
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
# for the stacking convention we use:
# x = x coordinate
# y = y coordinate
# c = image channel (e.g. multiple color channels)
# z = z coordinate
# t = time coordinate (for time lapse data)
##########################################################################################

import sys
import time
import datetime
import os
import math
import numpy as np
import glob

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
RAWDIR = os.path.join(BASEDIR, 'raw')
OUTDIR = os.path.join(BASEDIR, 'out')

if __name__ == '__main__':

    ######################################################################################
    # user settings
    
    # file type specifier
    FILETYPE = '/*.tif'
    
    # specify glob directory: all file matching FILETYPE will be considered  
    IMAGEDIR = RAWDIR # glob directory
    
    outname = 'stack_wCalibration.tif'

    image_width  = 628 # px
    image_height = 628 # px
    
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

    # set up metadata
    metadata = {'spacing' : 2.5,
                'unit': 'micron',\
                'axes': 'TZCXY'}
    
    ######################################################################################
    
    ensure_dir(os.path.join(BASEDIR, OUTDIR))

    xResFactor = float(x_resolution[0]) / float(x_resolution[1])
    yResFactor = float(y_resolution[0]) / float(y_resolution[1])
    resolution = (xResFactor, yResFactor)

    # load data
    filelist = []
    
    for filename in glob.glob(IMAGEDIR + FILETYPE):
            
        filelist.append(filename)
     
    # assuming that all *.tif files in the given directory belong to one z-stack   
    nSlices = len(filelist)
    
    print "==> using", nSlices, "z slices"
   
    # create empty stack
    stack = np.zeros((1, nSlices, 1, image_width, image_height), dtype = 'uint8')
    
    # iterate over all raw *.tif files
    for i, filename in enumerate(filelist):
        
        im = io.imread(filename)
        
        assert im.shape == (image_width, image_height)
        
        stack[0, i, 0, :, :] = im

    # the photometric keyword specifies the image colorspace
    tifffile.imsave(os.path.join(OUTDIR, outname), 
                    stack, 
			        imagej = True,
			        resolution = resolution,
			        metadata = metadata,
			        phptometric = 'minisblack')
            
        











 


    

            

		
		
		
		
		
		