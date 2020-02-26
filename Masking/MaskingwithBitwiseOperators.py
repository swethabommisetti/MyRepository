import cv2
import numpy as np
import blur_face_params as bf

image = bf.image
cv2.imshow("image", image)
cv2.waitKey(0)
print(image.shape[1])
print(image.shape[0])
mask = np.zeros(image.shape[:2], dtype=np.uint8)
#print(mask.shape)
cv2.rectangle(mask,bf.rect_start_pix, bf.rect_end_pix, (256,256,256), -1)
cv2.imshow("mask- extract face", mask)
cv2.waitKey(0)
outputImage = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("outputImage", outputImage)
cv2.waitKey(0)