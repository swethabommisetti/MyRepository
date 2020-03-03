import cv2
import numpy

#kernel creation
kernel=cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))# eroding a logo
image=cv2.imread("logo.png")
cv2.imshow("image", image)
cv2.waitKey(0)
for i in range (0, 3):
    Erodedimage=cv2.erode(image, kernel, i+5)
    cv2.imshow("eroded {} times".format(i+1), Erodedimage)
    cv2.waitKey(0)
# dilating an image
(T, threshInv) = cv2.threshold(image, 200, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Threshold Binary", threshInv)
cv2.waitKey(0)

for i in range (0, 3):
    DilatedImage= cv2.dilate(image, kernel, iterations= i+3)# using a 10 * 10 kernel
    cv2.imshow("dilated {} times".format(i), DilatedImage)
    cv2.waitKey(0)

#opening the links of image
for i in range (0, 3):
    OpenedImage = cv2.morphologyEx(threshInv, cv2.MORPH_OPEN, kernel, iterations=i+2)
    cv2.imshow("opened {} times".format(i), OpenedImage)
    cv2.waitKey(0)

#closing the empty or gaps in between an image

for i in range(0, 3):
     ClosedImage=cv2.morphologyEx(OpenedImage, cv2.MORPH_CLOSE, kernel)
     cv2.imshow("closed {} times".format(i), ClosedImage)
     cv2.waitKey(0)

#image = cv2.imread("ParkingLot.png")
image = cv2.imread("HatImage.png")

cv2.imshow("HatImage", image)
cv2.waitKey(0)
#BlackHat
BlackHat=cv2.morphologyEx(image, cv2.MORPH_BLACKHAT, kernel)
cv2.imshow("BlackHat", BlackHat)
cv2.waitKey(0)

#whiteHat
WhiteHat=cv2.morphologyEx(image, cv2.MORPH_TOPHAT, kernel)
cv2.imshow("WhiteHat", WhiteHat)
cv2.waitKey(0)