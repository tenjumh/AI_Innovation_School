import cv2
import numpy as np

img0 = cv2.imread('./image/add1.jpg', cv2.IMREAD_COLOR)
img1 = cv2.imread('./image/add2.jpg', cv2.IMREAD_COLOR)

cv2.imshow('img0', img0)
cv2.imshow('img1', img1)
cv2.waitKey()

num_images = 100

for i in range(999):
    # w0 = 0.001
    w0 = (i%num_images) / (num_images-1)
    w1 = 1 - w0
    img = cv2.addWeighted(img0, w0, img1, w1, 0)
    # print(w0)
    cv2.imshow('img', img)
    if cv2.waitKey(50) > -1: break
    #w0 *= i
    #print(w0)

