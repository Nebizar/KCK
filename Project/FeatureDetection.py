# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 17:50:47 2018

@author: Krzysztof Pasiewicz
"""
# OpenCV feature detection -> Millenium Falcon

#Basic libraries
import cv2 #-> OpenCV
import numpy as np

# Loading image
img = cv2.imread("MF1.jpg", cv2.IMREAD_GRAYSCALE)

surf = cv2.xfeatures2d.SURF_create()

keypoints, descriptors = surf.detectAndCompute(img, None)

img = cv2.drawKeypoints(img, keypoints, None)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
