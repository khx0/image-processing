#!/usr/bin/python
# -*- coding: utf-8 -*-
##########################################################################################
# author: Nikolas Schnellbaecher
# contact: khx0@posteo.net
# date: 2018-07-17
# file: extract_zstacks.py
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

from skimage import io
import skimage

def ensure_dir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)

now = datetime.datetime.now()
now = "%s-%s-%s" %(now.year, str(now.month).zfill(2), str(now.day).zfill(2))

BASEDIR = os.path.dirname(os.path.abspath(__file__))
RAWDIR = os.path.join(BASEDIR, 'raw')
OUTDIR = os.path.join(BASEDIR, 'out')

outdir = 'zstacks'
outname = 'zstack_at_frame_t_'
ZFILL = 3 # zero padding

ensure_dir(os.path.join(BASEDIR, outdir))
 
if __name__ == '__main__':
    
    filename = 'path/to/input-5D-stack.tif'
    
    print filename
    
    im = io.imread(filename)
    
    print im.shape
    
    nFrames = im.shape[0]
    
    # ensure that the 5D stacking convention is valid and change if needbe
    print "nFrames =", nFrames
    
    for i in range(nFrames):
	
	    outname = os.path.join(outdir, outname + str(i + 1).zfill(ZFILL) + '.tif')
	    
	    tmp = im[i]
	
	    print i, tmp.shape
	
	    io.imsave(outname, tmp)
	
	
	
	
	
	
	
	
	