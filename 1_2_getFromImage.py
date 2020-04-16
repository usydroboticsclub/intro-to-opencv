import cv2

frame = cv2.imread ("image.png")

cv2.imshow("loaded image", frame) # display it
cv2.waitKey(-1) # Wait indefinitely until the user presses a key.