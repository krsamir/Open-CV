import cv2

# For Images
img = cv2.imread('Resources/Cars.webp')        # Reading Image
cv2.imshow('Output',img)                        #Displayng Image
cv2.waitKey(0)                                  #Adding Delay


# For Videos
cap = cv2.VideoCapture('Resources/video.mp4')
while True:
    success, img = cap.read()        # Images will be saved in variable img and success variable will
                                     # tell the status
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# For Webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)                   #Setting Size
cap.set(4, 480)
cap.set(10, 100) # 10 for brightness
# 3 and 4 are id numbers which are id's for height and width
while True:
    success, img = cap.read()        # Images will be saved in variable img and success variable will
                                     # tell the status
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break