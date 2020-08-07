import cv2
import numpy as np
img = cv2.imread('Resources/cars.webp')  # Reading Image
kernel = np.ones((5, 5),np.uint8)    #Defining type of object unsigned integer of 8-bit

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Converts images to different color bases
imgBlur = cv2.GaussianBlur(img, (7, 7), 0)  # Adding Blur Image
imgCanny = cv2.Canny(img, 100, 100)
imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)
imgEroded = cv2.erode(imgDialation,kernel,iterations=1)

cv2.imshow('Gray Image', imgGray)                        #Displayng Image
cv2.imshow('Blur Image', imgBlur)
cv2.imshow('Edge Detection Image', imgCanny)
cv2.imshow('Dilation Image', imgDialation)
cv2.imshow('Erosion Image', imgEroded)

cv2.waitKey(0)                                   #Adding Delay
