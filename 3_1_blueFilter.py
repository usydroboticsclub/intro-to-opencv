import cv2
import numpy as np
frame = cv2.imread ("image.png")

frame[:,:,2]=np.zeros(frame[:,:,2].shape,frame.dtype)# remove the red
frame[:,:,1]=np.zeros(frame[:,:,1].shape,frame.dtype)# and the green
# notice that since the indexing is [x,y,channel] we want all (i.e. :) the x and all the y but one specific channel.

cv2.imshow("blue only", frame) # display it
cv2.waitKey(-1) # Wait indefinitely until the user presses a key.