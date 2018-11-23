# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 18:08:28 2018

@author: Krzystof Pasiewicz
"""
## Feature Detector - Millenium Falcon
import cv2
import numpy as np
from matplotlib import pyplot as plt

img1 = cv2.imread("falcon72.jpg", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("falcon105.jpg", cv2.IMREAD_GRAYSCALE)

surf = cv2.xfeatures2d.SURF_create()

keypoints1, descriptors1 = surf.detectAndCompute(img1, None)
keypoints2, descriptors2 = surf.detectAndCompute(img2, None)
##BEST
"""sift = cv2.xfeatures2d.SIFT_create()

keypoints1, descriptors1 = sift.detectAndCompute(img1, None)
keypoints2, descriptors2 = sift.detectAndCompute(img2, None)"""

"""orb = cv2.ORB_create()

keypoints1 = orb.detect(img1, None)
keypoints1, descriptors1 = orb.compute(img1, keypoints1)
keypoints2 = orb.detect(img2, None)
keypoints2, descriptors2 = orb.compute(img2, keypoints2)"""

# Brute Force Matching
bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck = False)
matches = bf.match(descriptors1, descriptors2)
matches = sorted(matches, key = lambda x:x.distance)

matching_result = cv2.drawMatches(img1, keypoints1, img2, keypoints2, matches, None, flags = 2)

# cv2.imshow("Falcon1", img1)
# cv2.imshow("Falcon2", img2)
#cv2.imshow("Maching", matching_result)

plt.imshow(matching_result,)
plt.axis('off')
plt.savefig("BFMatchSURF.png")
plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()


