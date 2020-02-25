import numpy as np
import cv2
import ImageSharpnessParams as isp

cv2.imshow("originalImage", isp.image)
cv2.waitKey(0)

#increasing image's intensity


ratio= 100 / isp.image.shape[1]
diamensions= (100, int(isp.image.shape[1] * ratio))
thumbnail= cv2.resize(isp.image, diamensions, interpolation= cv2.INTER_AREA)
cv2.imshow("small image", thumbnail)
cv2.waitKey(0)

intensity=np.zeros(thumbnail.shape, dtype= "uint8") + 200

added = cv2.add(thumbnail, intensity)
cv2.imshow("BrightImage", added)
cv2.waitKey(0)

#increasing contrast

addedbynp = np.add(thumbnail, intensity)
cv2.imshow("wrap_up", addedbynp)
cv2.waitKey(0)