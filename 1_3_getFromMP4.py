"""
You can also load videos from a video source, like so:
"""

import cv2 

cam = cv2.VideoCapture("videosample.mp4")

isOK=True
while isOK:
    isOK, frame = cam.read()
    if isOK:
        cv2.imshow("video frame", frame)
        cv2.waitKey(1) 


"""
You may notice the video is a lot faster that you would be seeing if you watched it. That's because openCV 
doesnt need to care about the framerate of the original video. You can tweak the waitKey until the video matches 
the framerate you want to process at.
"""