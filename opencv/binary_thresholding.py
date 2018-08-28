##########################################################################################
# author: Nikolas Schnellbaecher
# contact: nikolas.schnellbaecher@bioquant.uni-heidelberg.de
# date: 2018-08-28
# file: binary_thresholding.py
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
import matplotlib.pyplot as plt

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

    filename = 'test_image.png'

    img = cv2.imread(os.path.join(RAWDIR, filename))

    print("RGB image shape =", img.shape)

    # convert RGB 3 channel image to grayscale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    print("Grayscale image shape =", img_gray.shape)
    
    # binary thresholding
    # the cv2.threshold
    ret, thresh = cv2.threshold(img_gray, 22.0, 255, 0)
    
    print("Threshold image shape =", thresh.shape)

    # plot thresholded image
    fig, ax = plt.subplots()

    ax.imshow(thresh, 
              interpolation = 'nearest',
              cmap = plt.cm.gray)

    plt.show()

    
    
    
    