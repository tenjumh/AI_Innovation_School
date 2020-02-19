import cv2
import numpy as np

h = 480
w = 640

img = np.zeros(shape=(h, w, 3), dtype=np.uint8)

# 색을 넣어보자
img[h*0//3:h*1//3,:] = (255,0,0)
img[h*1//3:h*2//3,:] = (0,255,0)
img[h*2//3:h*3//3,:] = (0,0,255)
cv2.imshow('img', img)

img2 = np.zeros(shape=(h, w, 3), dtype=np.uint8)

# 네모를 넣어보자
img2[h*1//3:h*2//3,w*1//3:w*2//3] =(0,255,0)
cv2.imshow('img2', img2)
cv2.waitKey()

cv2.imwrite('./image/img.png', img)