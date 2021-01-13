"""
Given our previous results, there are specks of noise here and there which aren't shapes. Since we know that the shapes 
are bigger than a given size, we can remove many of the specks using morphological transformations. The two we will be using 
are erosion() and dilation(). Erosion means to wear away the outside of a group of pixels; if the pixels are too small, they wil 
be deleted. Dilation is the opposite, which we will need to do since we lose some area if we simply erode.
"""


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

#Copy a noise removed version
noiseDownMask=np.array(mask)
noiseDownFrame=np.array(frame)








kernel = np.ones((5,5),np.uint8) # the 5 by 5 tells the computer how much to erode by.
noiseDownMask = cv2.erode(noiseDownMask,kernel,iterations = 1)

noiseDownMask = cv2.dilate(noiseDownMask,kernel,iterations = 1)

# the mask is only 2D so we need to and it with each channel of H,S,V
frame[:,:,0] = cv2.bitwise_and(frame[:,:,0],mask)
frame[:,:,1] = cv2.bitwise_and(frame[:,:,1],mask)
frame[:,:,2] = cv2.bitwise_and(frame[:,:,2],mask)


# the mask is only 2D so we need to and it with each channel of H,S,V
noiseDownFrame[:,:,0] = cv2.bitwise_and(noiseDownFrame[:,:,0],noiseDownMask)
noiseDownFrame[:,:,1] = cv2.bitwise_and(noiseDownFrame[:,:,1],noiseDownMask)
noiseDownFrame[:,:,2] = cv2.bitwise_and(noiseDownFrame[:,:,2],noiseDownMask)

# convert it back into the original color space
frame = cv2.cvtColor(frame,cv2.COLOR_HSV2BGR)
noiseDownFrame = cv2.cvtColor(noiseDownFrame,cv2.COLOR_HSV2BGR)

cv2.imshow("blue only", frame) # display it
cv2.imshow("blue only, noise reduced", noiseDownFrame) # display it
cv2.waitKey(-1) # Wait indefinitely until the user presses a key.