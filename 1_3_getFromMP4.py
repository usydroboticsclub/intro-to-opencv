import cv2 

cam = cv2.VideoCapture("videosample.mp4")

isOK=True
while isOK:
    isOK, frame = cam.read()
    if isOK:
        cv2.imshow("video frame", frame)
        cv2.waitKey(1) 