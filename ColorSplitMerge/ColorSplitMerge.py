import cv2
import numpy as np

image=cv2.imread("faces.png")
cv2.imshow("image", image)
cv2.waitKey(0)
(B, G, R) = cv2.split(image)

cv2.imshow("b", B)
cv2.waitKey(0)

cv2.imshow("g", G)
cv2.waitKey(0)

cv2.imshow("r", R)
cv2.waitKey(0)

zeros = np.zeros(image.shape[:2], dtype = np.uint8)
cv2.merge([zeros,zeros,R])
cv2.imshow("r", R)
cv2.waitKey(0)

cv2.merge([B,zeros,zeros])
cv2.imshow("b", B)
cv2.waitKey(0)

cv2.merge([zeros,G,zeros])
cv2.imshow("G", G)
cv2.waitKey(0)