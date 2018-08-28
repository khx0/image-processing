#!/usr/bin/python
# -*- coding: utf-8 -*-
##########################################################################################
# author: Nikolas Schnellbaecher
# contact: nikolas.schnellbaecher@bioquant.uni-heidelberg.de
# date: 2018-08-28
# file: opencv_loader.py
# requires: OpenCV
# https://opencv.org
# Tested with Python 3.7.0 and OpenCV version 3.4.2
##########################################################################################

import sys
import time
import datetime
import os
import math
import numpy as np

# import OpenCV python bindings
import cv2 

def ensure_dir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)

now = datetime.datetime.now()
now = "%s-%s-%s" %(now.year, str(now.month).zfill(2), str(now.day).zfill(2))

BASEDIR = os.path.dirname(os.path.abspath(__file__))
RAWDIR = os.path.join(BASEDIR, 'raw')
OUTDIR = os.path.join(BASEDIR, 'out')

ensure_dir(RAWDIR)

if __name__ == '__main__':

    print("Woking with OpenCV version:", cv2.__version__)
    
    filename = 'test_image.png'
    
    img = cv2.imread(os.path.join(RAWDIR, filename))
    
    print("Image shape =", img.shape)

    
    