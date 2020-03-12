import cv2
import numpy as np

image= cv2.imread("car.png")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image= cv2.GaussianBlur(image, (5,5), 0)
cv2.imshow("image", image)
def auto_canny_function(image, sigma):
    if sigma == None:
       sigma= 0.33
    m =  np.median(image)
    lower = int(max(0, (1.0 - sigma) * m))
    upper = int(min(255, (1.0 + sigma) * m))
    edge = cv2.Canny(image, lower, upper)
    return edge

edge = auto_canny_function(image, None)
cv2.imshow("edge", edge)
cv2.waitKey(0)