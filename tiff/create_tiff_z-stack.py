#!/usr/bin/python
# -*- coding: utf-8 -*-
##########################################################################################
# author: Nikolas Schnellbaecher
# contact: khx0@posteo.net
# date: 2018-08-01
# file: create_tiff_z-stack.py
# requires scikit-image
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
    
    outname = 'stack.tif'
    
    # Takes all tif images in a specified directory and stacks them together.
    # As of now, this will create a z-stack from planar 2d images without calibration.
    
    ######################################################################################
    
    ensure_dir(os.path.join(BASEDIR, OUTDIR))
        
    with tifffile.TiffWriter(os.path.join(OUTDIR, outname)) as stack:
        
        for filename in glob.glob(IMAGEDIR + FILETYPE):
            
            stack.save(tifffile.imread(filename), photometric = 'minisblack')


		
		
		
		
		
		