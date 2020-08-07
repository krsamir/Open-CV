import cv2
import numpy as np

img = cv2.imread("Resources/Cars.webp")
print(img.shape)  # Finding the size of the image
'''So the output for img.show is (700, 1050, 3) where 700 is the height, 1050 is the width and 
3 is the number of channels.'''
imgResize = cv2.resize(img, (360, 640))  # Width, Height
# Cropping Image
imgCropped = img[0:500, 200:700]  # Height, width

cv2.imshow("Image", img)
cv2.imshow("Image Resize", imgResize)
cv2.imshow("Cropped Image", imgCropped)
cv2.waitKey(0)
