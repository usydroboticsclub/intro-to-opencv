import cv2
import numpy as np
frame = cv2.imread ("image.png")

cv2.imshow("original", frame) # display it

frame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) # You can find colour code conversions here: https://docs.opencv.org/master/d8/d01/group__imgproc__color__conversions.html

# define range of blue color in HSV
lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])

# Threshold the HSV image to get only blue colors
mask = cv2.inRange(frame, lower_blue, upper_blue)
# the mask is only 2D so we need to and it with each channel of H,S,V
frame[:,:,0] = cv2.bitwise_and(frame[:,:,0],mask)
frame[:,:,1] = cv2.bitwise_and(frame[:,:,1],mask)
frame[:,:,2] = cv2.bitwise_and(frame[:,:,2],mask)

# convert it back into the original color space
frame = cv2.cvtColor(frame,cv2.COLOR_HSV2BGR)

cv2.imshow("blue only", frame) # display it
cv2.waitKey(-1) # Wait indefinitely until the user presses a key.