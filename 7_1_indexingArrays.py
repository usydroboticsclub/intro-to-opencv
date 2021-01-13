"""
Indexing Arrays
"""

import cv2
import numpy as np

frame = cv2.imread("windows.png") # This variable is a 3D array which contains the BGR colour code for each pixel

print("The height of this array is {} pixels".format(frame.shape[0])) # The height axis is the "0" axis
print("The width of this array is {} pixels".format(frame.shape[1])) # The width axis is the "1" axis

print(frame[160,160]) # The output of this line is the colour code for a pixel red section of the logo in BGR format, which has coordinates somewhere in the top left of the screen.


####Exercises####
# Find the colour code of the other three sections of the logo.