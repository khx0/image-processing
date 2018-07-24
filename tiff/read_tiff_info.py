#!/usr/bin/python
# -*- coding: utf-8 -*-
##########################################################################################
# author: Nikolas Schnellbaecher
# contact: khx0@posteo.net
# date: 2018-07-24
# file: read_tiff_info.py
# useful to obtain meta data e.g. for tiff image file calibration
# The tif.info() command print a sequence of strings with meta data tags
# see https://github.com/scikit-image/scikit-image/blob/master/skimage/external/ \
# tifffile/tifffile.py#L1894
# for a more detailed reference of this command
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
RAWDIR = os.path.join(BASEDIR, 'raw')
OUTDIR = os.path.join(BASEDIR, 'out')
 
if __name__ == '__main__':
    
    ######################################################################################
    # user settings
    
    filename = 'path/to/myFile.tif'
    
    print "loading ...", filename
    
    ######################################################################################
    
    with TiffFile(filename) as tif:
        
        data = tif.asarray()
        
        print data.shape
        
        nFrames = data.shape[0]
    
        print "nFrames =", nFrames
        
        print tif.info()




        