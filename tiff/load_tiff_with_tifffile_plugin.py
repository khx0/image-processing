#!/usr/bin/python
# -*- coding: utf-8 -*-
##########################################################################################
# author: Nikolas Schnellbaecher
# contact: khx0@posteo.net
# date: 2018-07-24
# file: load_tiff.py
# requires scikit-image
##########################################################################################

import sys
import time
import datetime
import os
import math
import numpy as np

from skimage import io

def ensure_dir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)

now = datetime.datetime.now()
now = "%s-%s-%s" %(now.year, str(now.month).zfill(2), str(now.day).zfill(2))

BASEDIR = os.path.dirname(os.path.abspath(__file__))
RAWDIR = os.path.join(BASEDIR, 'raw')
OUTDIR = os.path.join(BASEDIR, 'out')
 
if __name__ == '__main__':
    
    filename = 'path/to/myFile.tif'
    
    print "opening ...", filename

    print io.plugin_info("tifffile")

    im = io.imread(filename, plugin = "tifffile")
    
    print im.shape
    
    