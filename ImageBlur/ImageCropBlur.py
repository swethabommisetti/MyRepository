import numpy as np
import argparse
import cv2
import blur_face_params as bfp

image =cv2.imread("for_blur.png")
blue=(255,0,0)

cv2.rectangle(image, bfp.rect_start_pix, bfp.rect_end_pix, blue)
cv2.imshow("image", image)
cv2.waitKey(0)

face = image[bfp.rect_start_pix[1]:bfp.rect_end_pix[1], bfp.rect_start_pix[0]:bfp.rect_end_pix[0]]
#gaussian blur
face = cv2.GaussianBlur(face,bfp.kernel_size, bfp.kernel_border)
cv2.imshow("sub_face", face)
cv2.waitKey(0)
image[bfp.rect_start_pix[1]:bfp.rect_start_pix[1]+face.shape[0], bfp.rect_start_pix[0]:bfp.rect_start_pix[0]+face.shape[1]] = face
cv2.imshow("gaussian blur", image)
cv2.waitKey(0)

#simple blur
face = cv2.blur(face,bfp.kernel_size, bfp.kernel_border)
cv2.imshow("simple blur", face)
cv2.waitKey(0)
image[bfp.rect_start_pix[1]:bfp.rect_start_pix[1]+face.shape[0], bfp.rect_start_pix[0]:bfp.rect_start_pix[0]+face.shape[1]] = face
cv2.imshow("gaussian blur", image)
cv2.waitKey(0)

#median blur
face = cv2.medianBlur(face, 3)
#face = cv2.medianBlur(face.astype(np.float32),3)
cv2.imshow("median blur", face)
cv2.waitKey(0)
image[bfp.rect_start_pix[1]:bfp.rect_start_pix[1]+face.shape[0], bfp.rect_start_pix[0]:bfp.rect_start_pix[0]+face.shape[1]] = face
cv2.imshow("gaussian blur", image)
cv2.waitKey(0)

#Bilateral blur
face = cv2.bilateralFilter(face, 21, 61, 13, bfp.kernel_border)# diameter, color, space
cv2.imshow("bilateral blur", face)
cv2.waitKey(0)
image[bfp.rect_start_pix[1]:bfp.rect_start_pix[1]+face.shape[0], bfp.rect_start_pix[0]:bfp.rect_start_pix[0]+face.shape[1]] = face
cv2.imshow("bilateral blur", image)
cv2.waitKey(0)