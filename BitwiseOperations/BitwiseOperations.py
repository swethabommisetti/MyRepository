import cv2
import numpy as np

#identifying empty spots in parking lot and represent them as white blocks
image=cv2.imread("ParkingLot.png")
cv2.imshow("Parking Lot" , image)
cv2.waitKey(0)
print(image.shape[0])
print(image.shape[1])
cv2.rectangle(image, (0,0), (45,90), (255,255,255), -1)
cv2.imshow("Parking Lot" , image)
cv2.waitKey(0)

#using bitwise operators and to identify occupied spots
carimage = cv2.imread("car.png")
cv2.imshow("parked car" , carimage)
cv2.waitKey(0)

"""
#using bitwise and operator
#we always fix our empty lot as white
emptylot1 = np.ones(carimage.shape, dtype="uint8") + 254
cv2.imshow("empty Lot1" , emptylot1)
cv2.waitKey(0)

BitwiseAnding=cv2.bitwise_and(emptylot1, carimage)
cv2.imshow("anding", BitwiseAnding)
cv2.waitKey(0)
#check if lot is empty by using a flag
lotemptyflag = cv2.subtract(emptylot1, BitwiseAnding)
cv2.imshow("lotemptyflag", lotemptyflag)
cv2.waitKey(0)
b, g, r = cv2.split(lotemptyflag)
if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
    print("lot is empty")
else:
    print("lot is occupied")
    

#using bitwise or
#we always fix our empty lot as black
emptylot1 = np.zeros(carimage.shape, dtype="uint8")
cv2.imshow("empty Lot1" , emptylot1)
cv2.waitKey(0)
Bitwiseoring=cv2.bitwise_or(emptylot1, carimage)
cv2.imshow("oring", Bitwiseoring)
cv2.waitKey(0)
lotemptyflag = cv2.add(emptylot1, Bitwiseoring)
cv2.imshow("lotemptyflag", lotemptyflag)
cv2.waitKey(0)
b, g, r = cv2.split(lotemptyflag)
if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
    print("lot is empty")
else:
    print("lot is occupied")

#using bit wise x-or
#we can fix our empty lot's color as always white or always black
#if we fix the empty lot's color as black then we follow the below logic
emptylot1 = np.ones(carimage.shape, dtype="uint8")
cv2.imshow("empty Lot1" , emptylot1)
cv2.waitKey(0)
xoring=cv2.bitwise_xor(emptylot1, carimage)
cv2.imshow("xoring", xoring)
cv2.waitKey(0)
lotemptyflag = cv2.add(emptylot1, xoring)
cv2.imshow("lotemptyflag", lotemptyflag)
cv2.waitKey(0)
b, g, r = cv2.split(lotemptyflag)
if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
    print("lot is empty")
else:
    print("lot is occupied")
    """
emptylot1 = np.ones(carimage.shape, dtype="uint8") + 254
cv2.imshow("empty Lot1", emptylot1)
cv2.waitKey(0)
xoring=cv2.bitwise_xor(emptylot1, carimage)
cv2.imshow("xoring", xoring)
cv2.waitKey(0)
lotemptyflag = cv2.subtract(emptylot1, xoring)
cv2.imshow("lotemptyflag", lotemptyflag)
cv2.waitKey(0)
b, g, r = cv2.split(lotemptyflag)
if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
    print("lot is empty")
else:
    print("lot is occupied")
