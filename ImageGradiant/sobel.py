# USAGE
# python sobel.py --image bricks.png

# import the necessary packages
import argparse
import cv2
import numpy as np


ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)
image= cv2.GaussianBlur(image, (5,5), 0)
gX = cv2.Sobel(image, ddepth=cv2.CV_16S,  dx=1, dy=0, ksize=3)
gY = cv2.Sobel(image, ddepth=cv2.CV_16S, dx=0, dy=1, ksize=3)
gX = cv2.convertScaleAbs(gX)
gY = cv2.convertScaleAbs(gY)
abs_sobelx = np.absolute(gX)
abs_sobely = np.absolute(gY)
sobelCombined = cv2.addWeighted(gX, 0.5, gY, 0.5, 0)
magnitude =  np.sqrt((gX**2) + (gY**2))
print("image's gradiant magnitude is {}".format(magnitude))
cv2.imshow("change is x-axis", gX)
cv2.imshow("change in y-axis", gY)
cv2.imshow("image outline", sobelCombined)
cv2.waitKey(0)
