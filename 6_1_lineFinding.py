"""
Finding Lines in Images
One of the many other things we can do with openCV is find the lines in an image. Here's what we do:
"""

import cv2
import numpy as np

frame = cv2.imread ("image.png")
edges = cv2.Canny(frame,100,200) # This uses the canny edge detector. The 100 and 200 are rather arbitrary parameters; the second should be larger than the first, play around to see what numbers work best for each image.


# Use the Canny again.

minLineLength=100
maxLineGap=10
edges = cv2.Canny(frame,100,200)
lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)

blankImage = np.zeros(frame.shape)
for l in lines:
    for x1,y1,x2,y2 in l:
        cv2.line(blankImage,(x1,y1),(x2,y2),(0,255,0),5)



cv2.imshow("original", frame)
cv2.imshow("lines", blankImage)
cv2.waitKey(-1)


"""
So this is able to find our image borders with some degree of accuracy.

This example and more are floating around the internet, but a good place to find them is:....
"""

####Exercises####
#   Challenge: Determine the road lane lines from a given image an drawing line onto them. 
#   Use the provided image lane_img.jpg from the Github as your testing image. 
#   Challenge: Draw the grid lines of the sudoku image by detecting the lines using a Hough transform.
#   Use image sudoku.png from the Github.