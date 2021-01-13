"""
Shape Finding 
Now, say we're making a valentines bot that wants to filter out lovehearts from an image. So far we've played around 
with colour, but how do we deal with shape?

Well, we can find the outline of shapes in our image using an edge detector. The edge detector will isolate pixels on 
the edges of shapes. Let's give it a go:
"""

import cv2
import numpy as np

frame = cv2.imread ("image.png")
edges = cv2.Canny(frame,100,200) # This uses the canny edge detector. The 100 and 200 are rather arbitrary parameters; the second should be larger than the first, play around to see what numbers work best for each image.

cv2.imshow("original", frame)
cv2.imshow("edges", edges) 
cv2.waitKey(-1)

"""
wow, art!
"""