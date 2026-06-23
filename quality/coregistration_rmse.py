import cv2
import numpy as np

# Read old and new images
img1 = cv2.imread("B4_old.tif", 0)
img2 = cv2.imread("B4.tif", 0)

# ORB detector
orb = cv2.ORB_create()

kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

# Match features
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(des1, des2)

# Calculate RMSE
errors = []

for m in matches:
    p1 = kp1[m.queryIdx].pt
    p2 = kp2[m.trainIdx].pt

    error = np.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
    errors.append(error)

rmse = np.sqrt(np.mean(np.square(errors)))

print(f"Coregistration RMSE: {rmse:.2f} pixels")