import numpy as np # Numpy is a numerical library in python. OpenCV is based in numpy and hence when doing low level operations we need numpy in our code.
import cv2

canvas = np.zeros((200,400,3),np.uint8) # Create a blank, black canvas in np.

cv2.fillPoly(canvas, [np.array([[50,50],[20,20],[50,20]])], (0, 0, 255)) # A triangle

cv2.polylines(canvas, [np.array([[110,110],[110,130],[130,130],[130,110]])], True, (255, 255, 0)) # A square

cv2.circle(canvas, (100,50),20,(255,0,0))

cv2.putText(canvas,"Hello world!", (20, 100), cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,255))
cv2.imshow("result",canvas)
cv2.waitKey(-1)
