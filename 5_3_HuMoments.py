import cv2
import numpy as np

frame = cv2.imread ("image.png")
edges = cv2.Canny(frame,100,200) # This uses the canny edge detector. The 100 and 200 are rather arbitrary parameters; the second should be larger than the first, play around to see what numbers work best for each image.


# Load another heart from a template
heart = cv2.imread("heart.png")
heartCanny = cv2.Canny(heart,100,200)
heartContours, hierarchy = cv2.findContours(heartCanny,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
heartBlank = np.zeros(heart.shape)
cv2.polylines(heartBlank,heartContours[1],True,(255),1)
# Find its contours and create a moment set for checking
heartMoments = cv2.moments(heartContours[1])
heartHuMoments= cv2.HuMoments(heartMoments)
print(heartHuMoments)

contours, hierarchy = cv2.findContours(edges,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
# Get rid of the ones with an area smaller than tiny

blankImage = np.zeros(edges.shape)

goodContours=[]
for contour in contours:
    if cv2.contourArea(contour)>100:
        contourMoments = cv2.moments(contour)
        contourHuMoments = cv2.HuMoments(contourMoments)
        delta = np.sum(heartHuMoments-contourHuMoments)
        if (np.abs(delta)<0.002):
            print(np.abs(delta))
            goodContours.append(contour)
            cv2.polylines(blankImage,contour,True,(255),1)

cv2.imshow("original", frame)
cv2.imshow("heart", heartBlank)
cv2.imshow("heartContour", heartCanny)
cv2.imshow("edges", edges) 
cv2.imshow("good contours", blankImage) 
cv2.waitKey(-1)