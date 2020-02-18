import cv2
import numpy as np

h = 480
w = 640

img = np.zeros(shape=(h, w, 3), dtype=np.uint8)
img[380:400,400:420] = (255,255,255)
cv2.imshow('img', img)

img1 =cv2.imread('./image/cat.jpg', cv2.IMREAD_UNCHANGED)
img1[:,:,2] = 0  # RGB에서 B를 0으로
cv2.imshow('img1', img1)
cv2.waitKey()