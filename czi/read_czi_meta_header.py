#!/usr/bin/python
# -*- coding: utf-8 -*-
##########################################################################################
# author: Nikolas Schnellbaecher
# contact: khx0@posteo.net
# date: 2018-08-02
# file: read_czi_meta_header.py
##########################################################################################
# requires czifile.py from Christoph Gohlke
# Christoph Gohlke <http://www.lfd.uci.edu/~gohlke/>
##########################################################################################

import sys
import time
import datetime
import os
import math
import numpy as np

from skimage import io
import skimage

from czifile import CziFile

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
    
    filename = 'myCziFile.czi'
    
    ######################################################################################
    
    print "loading ...", filename
    
    with CziFile(filename) as czi:
	
	print czi
	print czi.shape



	    