import cv2

"parameters for blurring only required face"
image=cv2.imread('for_blur.png')
rect_start_pix=(350,200)
rect_end_pix=(500, 356)
req_color=(0, 255, 0)
kernel_size=(23, 23)
kernel_border=30