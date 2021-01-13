import numpy as np # Numpy is a numerical library in python. OpenCV is based in numpy and hence when doing low level operations we need numpy in our code.
import cv2

canvas = np.zeros((200,400,3),np.uint8) # Create a blank, black canvas to draw on.

RED = (0,0,255) # A color is a set of 3 numbers that determine what (blue, green, red) are in a particular pixel. Red = no blue, no green, maximum red.
CYAN = (255,255,0)
BLUE = (255,0,0)
MAGENTA = (255,0,255)

cv2.fillPoly(canvas, [np.array([[50,50],[20,20],[50,20]])], RED) # A filled triangle

cv2.polylines(canvas, [np.array([[110,110],[110,130],[130,130],[130,110]])], True, CYAN) # A square

cv2.circle(canvas, (100,50),20,BLUE)

cv2.putText(canvas,"Hello world!", (20, 100), cv2.FONT_HERSHEY_SIMPLEX,1,MAGENTA)
cv2.imshow("result",canvas)
cv2.waitKey(-1)

#### Exercises ####
# 1. Try to draw a disney Mickey Mouse logo (a few circles) with openCV. Make it white on black.
# Think about how you can use the cv2.circle command to help ease the process. Have your window be a 600x600 size.
# 2. Now try to draw the logo black on white instead of white on black.
# 2. Draw an even more complex image using polygons and lines, and send us the image!
# 3. [CHALLENGE] Use the polylines function to draw a sine wave on a canvas.
# 4. [CHALLENGE] Make a little bouncing ball animation and save it to an mp4 file. This stackoverflow post might help:
# https://stackoverflow.com/questions/30509573/writing-an-mp4-video-using-python-opencv
