import cv2
import numpy as np
# Joining images
img = cv2.imread("Resources/cards.webp")

imgHor = np.hstack((img, img))
imgVer = np.vstack((img, img))
cv2.imshow("Image Horizontal", imgHor)
cv2.imshow("Image Vertical", imgVer)

cv2.waitKey(0)