import numpy as np
import argparse
import cv2
import blur_face_params as p

image =cv2.imread("for_blur.png")
blue=(255,0,0)
#cv2.rectangle(image, (200, 50), (225, 125), blue, -1)
#cv2.rectangle(image, (134, 200), (186, 218), (0, 0, 255), -1)
cv2.rectangle(image, p.rect_start_pix, p.rect_end_pix, blue)
cv2.imshow("image", image)
cv2.waitKey(0)
face = image[p.rect_start_pix[1]:p.rect_end_pix[1], p.rect_start_pix[0]:p.rect_end_pix[0]]
#face = image[200:356,350:500]
face = cv2.GaussianBlur(face,p.kernel_size, p.kernel_border)
cv2.imshow("sub_face", face)
cv2.waitKey(0)
#result_image[y:y+sub_face.shape[0], x:x+sub_face.shape[1]] = sub_face
image[p.rect_start_pix[1]:p.rect_start_pix[1]+face.shape[0], p.rect_start_pix[0]:p.rect_start_pix[0]+face.shape[1]] = face
cv2.imshow("blurred face", image)
cv2.waitKey(0)
