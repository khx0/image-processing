##########################################################################################
# author: Nikolas Schnellbaecher
# contact: nikolas.schnellbaecher@bioquant.uni-heidelberg.de
# date: 2018-08-28
# file: extract_contour.py
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
ensure_dir(OUTDIR)

if __name__ == '__main__':
    
    filename = 'test_image.png'
    
    outname = 'longest_contour_xy_data.txt'
    
    ######################################################################################

    img = cv2.imread(os.path.join(RAWDIR, filename))

    print("RGB image shape =", img.shape)

    # convert RGB 3 channel image to grayscale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    print("Grayscale image shape =", img_gray.shape)


    # binary thresholding
    ret, thresh = cv2.threshold(img_gray, 22.0, 255, 0)

    # contour extraction
    im2, contours, hierarchy = cv2.findContours(thresh, 
                                                cv2.RETR_TREE, 
                                                cv2.CHAIN_APPROX_SIMPLE)

    ######################################################################################
    # Find the longest contour in the given image
    # find longest contour
    longestContourIndex = 0
    print("Number of detected contours =", len(contours))
    for i, contour in enumerate(contours):
        # print(i, contour.shape)
        if (contour.shape[0] > contours[longestContourIndex].shape[0]):
            longestContourIndex = i
        
    contour = contours[longestContourIndex]  
    print("longest contour has index =", longestContourIndex)
    print("longest contour shape =", contour.shape)
    
    # reshape longest detected contour
    contour = contour.reshape(contour.shape[0], 2)
    print("longest contour reshaped shape =", contour.shape)
    ######################################################################################
    
    # save contour as xy pairs
    np.savetxt(os.path.join(OUTDIR, outname), contour, fmt = '%.8f')
    
    ######################################################################################
    # plot grayscale image and the longest detected contour
    fig, ax = plt.subplots()

    ax.plot(contour[:, 0], contour[:, 1])
    ax.imshow(img_gray, 
              interpolation = 'nearest',
              cmap = plt.cm.gray)

    plt.show()

    
    
    