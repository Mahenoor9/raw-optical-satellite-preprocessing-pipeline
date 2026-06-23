import cv2
import matplotlib.pyplot as plt

# Load images in grayscale
img1 = cv2.imread("B4.tif", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("B4 (1).tif", cv2.IMREAD_GRAYSCALE)

# Create ORB detector
orb = cv2.ORB_create()

# Detect keypoints and descriptors
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

# Match descriptors
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(des1, des2)

# Sort matches
matches = sorted(matches, key=lambda x: x.distance)

# Draw top 50 matches
matched_img = cv2.drawMatches(
    img1, kp1,
    img2, kp2,
    matches[:50],
    None,
    flags=2
)

# Show result
plt.figure(figsize=(15,8))
plt.imshow(matched_img)
plt.title("Feature Matching Between Two Dates")
plt.axis("off")
plt.show()