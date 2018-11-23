import numpy as np
import cv2
 
img = cv2.imread("falcon78.JPG", 0) # queryiamge
 
cap = cv2.VideoCapture("Clip2.mp4")
 
# Features
sift = cv2.xfeatures2d.SIFT_create()
(kp_image, desc_image) = sift.detectAndCompute(img, None)

 
# Feature matching
FLANN_INDEX_KDTREE = 1
index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
search_params = dict(checks=50)   # or pass empty dictionary
flann = cv2.FlannBasedMatcher(index_params,search_params)


while True:
    _, frame = cap.read()
    if frame is None:
        print("THE END")
        break
    grayframe = cv2.cvtColor(frame, 0) # trainimage
    
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
    if len(good_points) > 20:
        query_pts = np.float32([kp_image[m.queryIdx].pt for m in good_points]).reshape(-1, 1, 2)
        train_pts = np.float32([kp_grayframe[m.trainIdx].pt for m in good_points]).reshape(-1, 1, 2)
 
        matrix, mask = cv2.findHomography(query_pts, train_pts, cv2.RANSAC, 5.0)
        matches_mask = mask.ravel().tolist()
 
        # Perspective transform
        h, w = img.shape
        pts = np.float32([[0, 0], [0, h-1], [w-1, h-1], [w-1, 0]]).reshape(-1, 1, 2)
        if matrix is None:
            print("NoneType Error #2")
            continue
        dst = cv2.perspectiveTransform(pts, matrix)
 
        homography = cv2.polylines(frame, [np.int32(dst)], True, (255, 0, 0), 3)
 
        cv2.imshow("StarWarsTracker", homography)
    else:
        cv2.imshow("StarWarsTracker", grayframe)
 
 
 
    #cv2.imshow("Image", img)
    #cv2.imshow("grayFrame", grayframe)
    #cv2.imshow("img3", img3)
 
    key = cv2.waitKey(1)
    if key == 27:
        break
 
cap.release()
cv2.destroyAllWindows()