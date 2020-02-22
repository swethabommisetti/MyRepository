import numpy as np
import imutils
import cv2
import argparse
import ParamsRotation as pr

#image = cv2.imread("Upsidedownillusion.png")
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

# lrotating an image 180 degrees
input_image = cv2.imread(args["image"])
cv2.imshow("Original", input_image)
cv2.waitKey(0)
(h, w) = input_image.shape[:2]
(cX, cY) = (w / 2, h / 2)
M = cv2.getRotationMatrix2D((cX, cY), pr.deg, pr.axis)
rotated = cv2.warpAffine(input_image, M, (w, h))
cv2.imshow("Rotated by 180 Degrees", rotated)
cv2.waitKey(0)

#translation of image

for i in range(1, 20):
    pr.i=pr.i+10
    pr.j=pr.j+10
    matrix = np.float32([[1, 0, pr.i], [0, 1, pr.j]])
    #cv2.warpAffine(input_image, matrix, (w, h))
    shifted = cv2.warpAffine(input_image, matrix, (input_image.shape[1], input_image.shape[0]))
    cv2.imshow("shifted image", shifted)
    cv2.waitKey(pr.waitime)