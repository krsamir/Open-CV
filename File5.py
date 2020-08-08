import cv2
import numpy as np

# Warp Perspective
img = cv2.imread("Resources/cards.webp")
width, height = 250, 350
pts1 = np.float32([[240, 38], [346, 107], [134, 188], [235, 263]])  # the points of the object
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
imageOutput = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Image", img)
cv2.imshow("Warped Image", imageOutput)
cv2.imwrite('./warpedImage.jpeg', imageOutput)

cv2.waitKey(0)