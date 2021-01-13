"""
Filtering Colours 2
Ok, so we now have only the blue channel. But you'll notice that all the white parts of the original image are there too! 
That's because white is a combination of blue, green and red; and removing red and green means the red still sticks around.

What can we do instead? One way we can resolve this is changing the colour space. A colour space refers to a representation of 
colour. We're currently in a BGR colour space, but we can convert our image into a HSV colour space using openCV. HSV stands for 
Hue (colour), Saturation (vividness), Value(brightness). Next, we can filter out only things that have colour equal to blue. Here's 
the code:
"""

import cv2
import numpy as np
frame = cv2.imread ("image.png")

cv2.imshow("original", frame) # display it

frame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) # You can find colour code conversions here: https://docs.opencv.org/master/d8/d01/group__imgproc__color__conversions.html

cv2.imshow("hsv_messy",frame)

# define range of blue color in HSV
lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])

# Threshold the HSV image to get only blue colors
mask = cv2.inRange(frame, lower_blue, upper_blue)
cv2.imshow("mask",mask)

# the mask is only 2D so we need to and it with each channel of H,S,V
frame[:,:,0] = cv2.bitwise_and(frame[:,:,0],mask)
frame[:,:,1] = cv2.bitwise_and(frame[:,:,1],mask)
frame[:,:,2] = cv2.bitwise_and(frame[:,:,2],mask)

# convert it back into the original color space
frame = cv2.cvtColor(frame,cv2.COLOR_HSV2BGR)

cv2.imshow("blue only", frame) # display it
cv2.waitKey(-1) # Wait indefinitely until the user presses a key.

"""
That's a lot better than before!
"""

####Exercises####
# In this folder you'll find an image with blue and green Yin and Yangs among a forest background. Using this code and your own
# knowledge, create two new images: one with only blue Yin and Yangs and one with only green.

# Hint: the BGR values of lime green are [0,255,0] you'll need to convert these to HSV using the converter file in this folder. 