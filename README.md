# OpenCV tutorial
OpenCV is a toolkit for processing computer imagery. This tutorial covers some common jobs you can do using openCV. But first, a bit of context. OpenCV is NOT machine learning; instead, it is a series of algorithms made by humans that do certain tasks. They are not perfect, and you, as another human, have to make the most of them. Additionally, since OpenCV is a toolkit, it is not applicable in every scenario. 

What does this repository help you do? It assumes you have a windows/linux/macbook and know nothing except how to click stuff and type stuff. It will help you understand how to solve certain problems. Let's get started!


## Recording
The password for these recordings is 6mDDFSSjD#xY
The below links will expire on 30-10-2020 and will become unavailable for download after this date.
Audio Only (19.96 MB)
https://cloudstor.aarnet.edu.au/plus/s/iiyNVuxTEymapAA
Other (198.00 B)
https://cloudstor.aarnet.edu.au/plus/s/9HDKkqamVRAWTIw
Video (105.31 MB)
https://cloudstor.aarnet.edu.au/plus/s/wobyt7sqHmgoTz7


## Table of contents
1. How do I install OpenCV?
2. How do I get images from my camera / a file?
3. How do I show my results?
4. How do I single out a specific colour from my image?
5. How do I get rid of noise in my image?
6. How do I match a particular shape in my image?
7. How do I find lines in my image?
8. Where do I go for more info?

Before you start, you may want to clone this repository, as it has a number of useful sample images and code for you.

## Installing OpenCV
1. Install python. If you need step by step instructions doing this, check out our python tutorial: https://github.com/usydroboticsclub/python
2. Learn python. If you need step by step instructions doing this, check out our python tutorial: https://github.com/usydroboticsclub/python; and our other python tutorial: https://github.com/usydroboticsclub/py_harder
3. Open a command shell. All platforms have a command shell. If you're on windows, click the start menu and type CMD, then press enter. If you're on mac, go to launcher and type in Terminal. If you're on linux, press your equivalent of a start button and type in terminal.
4. Type in `pip install opencv-python` and press enter. You many have to wait a bit. 
5. Hooray! You now have opencv on your computer.

## Getting images from your camera or a file
You can get your images from a variety of sources. You can get an image from your camera (if you have one on your computer) using the following command:
```python
import cv2 # it's not called opencv, its called cv2, because its just faster

cam = cv2.VideoCapture(0) # The 0 is for the index of your camera. If you have multiple cameras, you may need to use something other than 0.

while (1):
    isOK, frame = cam.read() # get the image
    if isOK:
        cv2.imshow("camera shot", frame) # display it
        cv2.waitKey(1) # Wait for 1 millisec so that it doesnt cause the computer to hang indefinitely
``` 
That's a lot to take in, but hopefully each line is fairly straightforward.

If you don't have a camera, you can also use the `imread` command to get images from files:
```python
import cv2

frame = cv2.imread ("image.png")

cv2.imshow("loaded image", frame) # display it
cv2.waitKey(-1) # Wait indefinitely until the user presses a key.
``` 

You can also load videos from a video source, like so:
```python
import cv2 

cam = cv2.VideoCapture("videosample.mp4")

isOK=True
while isOK:
    isOK, frame = cam.read()
    if isOK:
        cv2.imshow("video frame", frame)
        cv2.waitKey(1) 
``` 
You may notice the video is a lot faster that you would be seeing if you watched it. That's because openCV doesnt need to care about the framerate of the original video. You can tweak the waitKey until the video matches the framerate you want to process at.


## Displaying things
Now, perhaps we want to not only show our image, but also highlight a certain portion of it. OpenCV provides a number of functions for doing that. Let's take a look at some:

```python
import numpy as np # Numpy is a numerical library in python. OpenCV is based in numpy and hence when doing low level operations we need numpy in our code.
import cv2

canvas = np.zeros(200,400,3) # Create a blank, black canvas in np.

cv2.fillPoly(canvas, [[50,50],[20,20],[50,20]], (255, 255, 255)) # A triangle

cv2.polyLine(canvas, [[110,110],[110,130],[130,130],[130,110]], (255, 255, 0)) # A square

cv2.circle(canvas, [100,50],20,(255,0,0))

cv2.putText(canvas,"Hello world!", [20, 100], cv2.FONT_HERSHEY_SIMPLEX,10,(255,0,255))
cv2.imshow(canvas)
cv2.waitKey(-1)
```
You can play around with the parameters to get different results. 

## Filtering colours
Let's go back to the image we had earlier with all the shapes. Let's say our robot needs to detect all the blue shapes in the image, because they're evil. How can we do this?

We need to first delve in to how the image is repesented. By default, images in openCV are defined as three sets of 2D arrays: a blue channel, a green channel and a red channel, in that order. We can take advantage of this here by just cutting away the red and green channels:

```python
import cv2
import numpy as np
frame = cv2.imread ("image.png")

cv2.imshow("original", frame) # display it

frame[:,:,2]=np.zeros(frame[:,:,2].shape,frame.dtype)# remove the red
frame[:,:,1]=np.zeros(frame[:,:,1].shape,frame.dtype)# and the green
# notice that since the indexing is [x,y,channel] we want all (i.e. :) the x and all the y but one specific channel.

cv2.imshow("blue only", frame) # display it
cv2.waitKey(-1) # Wait indefinitely until the user presses a key.
```
Ok, so we now have only the blue channel. But you'll notice that all the white parts of the original image are there too! That's because white is a combination of blue, green and red; and removing red and green means the red still sticks around. 

What can we do instead? One way we can resolve this is changing the colour space. A colour space refers to a representation of colour. We're currently in a BGR colour space, but we can convert our image into a HSV colour space using openCV. HSV stands for Hue (colour), Saturation (vividness), Value(brightness). Next, we can filter out only things that have colour equal to blue. Here's the code:

```python
import cv2
import numpy as np
frame = cv2.imread ("image.png")

cv2.imshow("original", frame) # display it

frame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) # You can find colour code conversions here: https://docs.opencv.org/master/d8/d01/group__imgproc__color__conversions.html

# define range of blue color in HSV
lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])

# Threshold the HSV image to get only blue colors
mask = cv2.inRange(frame, lower_blue, upper_blue)
# the mask is only 2D so we need to and it with each channel of H,S,V
frame[:,:,0] = cv2.bitwise_and(frame[:,:,0],mask)
frame[:,:,1] = cv2.bitwise_and(frame[:,:,1],mask)
frame[:,:,2] = cv2.bitwise_and(frame[:,:,2],mask)

# convert it back into the original color space
frame = cv2.cvtColor(frame,cv2.COLOR_HSV2BGR)

cv2.imshow("blue only", frame) # display it
cv2.waitKey(-1) # Wait indefinitely until the user presses a key.
```

That's a lot better than before!

## Getting rid of noise
Given our previous results, there are specks of noise here and there which aren't shapes. Since we know that the shapes are bigger than a given size, we can remove many of the specks using morphological transformations. The two we will be using are `erosion` and `dilation`. Erosion means to wear away the outside of a group of pixels; if the pixels are too small, they wil be deleted. Dilation is the opposite, which we will need to do since we lose some area if we simply erode. 

```python
# Starting from the mask from before: 

# Threshold the HSV image to get only blue colors
mask = cv2.inRange(frame, lower_blue, upper_blue)

kernel = np.ones((5,5),np.uint8) # the 5 by 5 tells the computer how much to erode by.
mask = cv2.erode(mask,kernel,iterations = 1)

mask = cv2.dilate(mask,kernel,iterations = 1)

# These two are used together so commonly that you can do them both in fewer lines:
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

```

## Shape finding
Now, say we're making a valentines bot that wants to filter out lovehearts from an image. So far we've played around with colour, but how do we deal with shape?

Well, we can find the outline of shapes in our image using an edge detector. The edge detector will isolate pixels on the edges of shapes. Let's give it a go:

```python
import cv2
import numpy as np

frame = cv2.imread ("image.png")
edges = cv2.Canny(frame,100,200) # This uses the canny edge detector. The 100 and 200 are rather arbitrary parameters; the second should be larger than the first, play around to see what numbers work best for each image.

cv2.imshow("original", frame)
cv2.imshow("edges", edges) 
cv2.waitKey(-1)
```
wow art!

Now, there's a lot of noise so far, because rightfully so there are a lot of edges from things that are not our shapes. We still need to find our lovehearts! To do this, we need to know which of these edge pixels should be grouped together to form actual shapes. Of course, there is a function for this:

```python
contours, hierarchy = cv2.findContours(edges,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
# Hierarchy is a list of which contours are contained in which. It can be useful sometimes.

blankImage = np.zeros(edges.shape)

# Get rid of the ones with an area smaller than tiny
goodContours=[]
for contour in contours:
    if cv2.contourArea(contour)>100:
        goodContours.append(contour)
        cv2.polylines(blankImage,contour,True,(255),1)
```

Great! We have less random noise and more shapes now. Next, we have to find all those hearts! Perhaps if we had a heart template, we could match the hearts in the image to the heart template. But all the hearts are of different sizes and rotations... 

Fortunately, people smarter than we figured out that certain functions of the x and y coordinates of an image are invariant to the size, scaling and rotation of a shape. These are called the Hu-moments of the image, and we'll use them to our advantage here.


```python
# Load another heart from a template
heart = cv2.imread("heart.png")
heartContours, hierarchy = cv2.findContours(heart[:,:,0],cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
# Find its contours and create a humoment set for checking
heartMoments = cv2.moments(heartCountours[0])
heartHuMoments = cv2.HuMoments(heartCountours[0])

# Check the heart moment against the moments of the contours we found before
for c in contours:
    contourMoments = cv2.moments(c)
    contourHuMoments = cv2.HuMoments(contourMoments)

    delta = np.sum(heartHuMoments-contourHuMoments)
    if (delta<0.002):
        # this is a shape we want.
        # 0.002 is an aribtrary value
```

## Finding lines in images
One of the many other things we can do with openCV is find the lines in an image. Here's what we do:

```python
# Use the Canny again.

minLineLength=100
maxLineGap=10
edges = cv2.Canny(frame,100,200)
lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)
for x1,y1,x2,y2 in lines[0]:
    cv2.line(frame,(x1,y1),(x2,y2),(0,255,0),2)
```
So this is able to find our image borders with some degree of accuracy.

This example and more are floating around the internet, but a good place to find them is:....

## Additional resources
* https://opencv-python-tutroals.readthedocs.io/en/latest/index.html: All of the above tutorials and more!
