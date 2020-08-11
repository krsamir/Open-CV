import cv2

faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
img = cv2.imread("Resources/face.png")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
'''
faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)
# loop around all faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
cv2.imshow("Face", img)
cv2.waitKey(0)
'''

# For Webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)                   #Setting Size
cap.set(4, 480)
cap.set(10, 100) # 10 for brightness
# 3 and 4 are id numbers which are id's for height and width
while True:
    success, img = cap.read()        # Images will be saved in variable img and success variable will
                                     # tell the status
    faces = faceCascade.detectMultiScale(img, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break