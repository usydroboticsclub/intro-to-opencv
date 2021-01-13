"""
Filtering colours 1
Let's go back to the image we had earlier with all the shapes. Let's say our robot needs to detect all the blue shapes in the 
image, because they're evil. How can we do this?

We need to first delve in to how the image is repesented. By default, images in openCV are defined as three sets of 2D arrays: 
a blue channel, a green channel and a red channel, in that order. We can take advantage of this here by just cutting away the red 
and green channels:
"""

import cv2
import numpy as np
frame = cv2.imread ("image.png") 
# If you are getting an error due to a 'Nonetype', your terminal is not working from the right directory, close and reopen VSCode, 
# but this time hit 'Open Folder' and select this lesson's folder.

frame[:,:,2]=np.zeros(frame[:,:,2].shape,frame.dtype)# remove the red
frame[:,:,1]=np.zeros(frame[:,:,1].shape,frame.dtype)# and the green
# notice that since the indexing is [x,y,channel] we want all (i.e. :) the x and all the y but one specific channel.

cv2.imshow("blue only", frame) # display it
cv2.waitKey(-1) # Wait indefinitely until the user presses a key.

