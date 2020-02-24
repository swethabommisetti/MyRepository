import argparse
import cv2
import numpy as np
import ImageResizeParams as irp

#image1 =cv2.imread("for_blur.png")
cv2.imshow("first image", irp.image1)
cv2.waitKey(200)
r = 150.0 / irp.image1.shape[1]
dim = (150, int(irp.image1.shape[0] * r))
resized1 = cv2.resize(irp.image1, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("Resized (Width)", resized1)
cv2.waitKey(200)


image2 =cv2.imread("for_resizing.png")
cv2.imshow("second image", irp.image2)
cv2.waitKey(200)
r = 150.0 / irp.image2.shape[1]
dim = (150, int(irp.image2.shape[0] * r))
resized2 = cv2.resize(irp.image2, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("Resized (Width)", resized2)
cv2.waitKey(200)

#creating a collage

collage = np.concatenate((resized1, resized2), axis=0)
cv2.imshow("collage", collage)
cv2.waitKey(0)
#trying to put resizing in a loop



