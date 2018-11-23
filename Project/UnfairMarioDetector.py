# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 16:32:07 2018

@author: Krzysztof Pasiewicz
"""
from PIL import ImageGrab
import numpy as np
import cv2

img_prim = cv2.imread("MarioTeam.JPG", 0)

# Features
sift = cv2.xfeatures2d.SIFT_create()
(kp_image, desc_image) = sift.detectAndCompute(img_prim, None)

 
# Feature matching
FLANN_INDEX_KDTREE = 1
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks=50)   # or pass empty dictionary
flann = cv2.FlannBasedMatcher(index_params,search_params)

while True:
    img = ImageGrab.grab(bbox=(250,100,1400,920)) #bbox specifies specific region (bbox= x,y,width,height *starts top-left)
    img_np = opencvImage = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR) #this is the array obtained from conversion
    #goodframe = cv2.cvtColor(img_np, cv2.COLOR_)
    grayframe = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
    
    
    (kp_grayframe, desc_grayframe) = sift.detectAndCompute(grayframe, None)
    if desc_grayframe is None:
        print("NoneType Error #1")
        continue
    #print(desc_grayframe.type())
    #print(desc_image.type())
    if len(kp_image)>=2 and len(kp_grayframe)>=2:
        matches = flann.knnMatch(desc_image, desc_grayframe, k=2)
    else:
        print("Too few keypoints ERROR")
        continue
 
    good_points = []
    for m, n in matches:
        if m.distance < 0.7*n.distance:
            good_points.append(m)
    print(len(good_points))
    # Homography
    if len(good_points) > 15:
        query_pts = np.float32([kp_image[m.queryIdx].pt for m in good_points]).reshape(-1, 1, 2)
        train_pts = np.float32([kp_grayframe[m.trainIdx].pt for m in good_points]).reshape(-1, 1, 2)
 
        matrix, mask = cv2.findHomography(query_pts, train_pts, cv2.RANSAC, 5.0)
        matches_mask = mask.ravel().tolist()
 
        # Perspective transform
        h, w = img_prim.shape
        pts = np.float32([[0, 0], [0, h-1], [w-1, h-1], [w-1, 0]]).reshape(-1, 1, 2)
        if matrix is None:
            print("NoneType Error #2")
            continue
        dst = cv2.perspectiveTransform(pts, matrix)
 
        homography = cv2.polylines(img_np, [np.int32(dst)], True, (255, 0, 0), 3)
 
        cv2.imshow("UnfairMario", homography)
    else:
        cv2.imshow("UnfairMario", grayframe)

    #cv2.imshow("test",grayframe)
    
    
    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()
    
