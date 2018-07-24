#!/usr/bin/python
# -*- coding: utf-8 -*-
##########################################################################################
# author: Nikolas Schnellbaecher
# contact: khx0@posteo.net
# date: 2018-07-23
# file: skimage_tifffile_imsave.py
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
from skimage.external import tifffile
from skimage.external.tifffile import TiffFile

def ensure_dir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)

now = datetime.datetime.now()
now = "%s-%s-%s" %(now.year, str(now.month).zfill(2), str(now.day).zfill(2))

BASEDIR = os.path.dirname(os.path.abspath(__file__))
RAWDIR = os.path.join(BASEDIR, 'raw')
OUTDIR = os.path.join(BASEDIR, 'out')
 
if __name__ == '__main__':

    filename = 'temp.tif'

    ######################################################################################

    data = np.random.rand(3, 301, 219)
    
    print data.shape
    
    tifffile.imsave(filename, data, photometric = 'minisblack')
    
    ######################################################################################
    
    image = tifffile.imread(filename)
    
    np.testing.assert_array_equal(image, data)
    
    print image.shape
    
    ######################################################################################
    
    with TiffFile(filename) as tif:
        
        images = tif.asarray()
        
        for page in tif.pages:
            
            for tag in page.tags.values():
                
                print tag.name, tag.value
                # _ = tag.name, tag.value
            
            image = page.asarray()

    
    
    