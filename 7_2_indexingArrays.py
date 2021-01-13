"""
Indexing Arrays
"""

import cv2
import numpy as np

frame = cv2.imread("windows.png")

for i in range(frame.shape[0]): # Creating a loop to parse through the height of the image
    for j in range(frame.shape[1]): # Now parsing through the width 
        if 0<= frame[i, j, 0] <= 20 and 180<=frame[i, j, 1] <= 200 and 235 <=frame[i, j, 2] <= 255: # Checking for pixels which lie within a range of values around the specific colour
            frame[i, j, 0] = 255 
            frame[i, j, 1] = 255
            frame[i, j, 2] = 255
            # Setting these pixels to white

cv2.imshow("edited", frame) # Displaying the new image
cv2.waitKey(-1) # This is required to show any image in cv2.


####Exercises####
# Change each of the colours of the logo to a new colour