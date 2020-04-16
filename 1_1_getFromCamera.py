 import cv2 # it's not called opencv, its called cv2, because its just faster

cam = cv2.VideoCapture(0) # The 0 is for the index of your camera. If you have multiple cameras, you may need to use something other than 0.

while (1):
    isOK, frame = cam.read() # get the image
    if isOK:
        cv2.imshow("camera shot", frame) # display it
        cv2.waitKey(1) # Wait for 1 millisec so that it doesnt cause the computer to hang indefinitely