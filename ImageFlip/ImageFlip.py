import cv2
import ImageFlipParams as ifp


cv2.imshow("original",ifp.image)
cv2.waitKey(0)
HorizantalFlip=cv2.flip(ifp.image, 1)
VerticalFlip=cv2.flip(ifp.image, 0)
HandVFlip=cv2.flip(ifp.image, -1)
cv2.imshow("HorizantalFlip", HorizantalFlip)
cv2.waitKey(0)
cv2.imshow("VerticalFlip", VerticalFlip)
cv2.waitKey(0)
cv2.imshow("HandVFlip", HandVFlip)
cv2.waitKey(0)