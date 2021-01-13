"""
Shape Finding 2
Now, there's a lot of noise so far, because rightfully so there are a lot of edges from things that are 
not our shapes. We still need to find our lovehearts! To do this, we need to know which of these edge pixels 
should be grouped together to form actual shapes. Of course, there is a function for this:
"""

import cv2
import numpy as np

frame = cv2.imread ("image.png")
edges = cv2.Canny(frame,100,200) # This uses the canny edge detector. The 100 and 200 are rather arbitrary parameters; the second should be larger than the first, play around to see what numbers work best for each image.

contours, hierarchy = cv2.findContours(edges,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
# Get rid of the ones with an area smaller than tiny

blankImage = np.zeros(edges.shape)

goodContours=[]
for contour in contours:
    if cv2.contourArea(contour)>100:
        goodContours.append(contour)
        cv2.polylines(blankImage,contour,True,(255),1)

cv2.imshow("original", frame)
cv2.imshow("edges", edges) 
cv2.imshow("big contours", blankImage) 
cv2.waitKey(-1)