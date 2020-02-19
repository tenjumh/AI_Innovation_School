import cv2
import numpy as np

mat0 = np.uint8([[130,140],[150,160]])
mat1 = np.uint8([[100,100],[100,100]])
mat2 = np.uint8([[145,145],[145,145]])
print('mat0'); print(mat0)
print('mat1\n', mat1)
print('mat2\n', mat2)

print('cv2.add(mat0, mat1)')
print(cv2.add(mat0, mat1))

print('cv2.subtract(mat0, mat2)')
print(cv2.subtract(mat0, mat2))

print('cv2.addWeighted(mat0, 0.7, mat1, 0.3, 0)')
cv2.addWeighted(mat0, 0.7, mat1, 0.3, 0)

################################################
img0 = cv2.imread('./image/add1.jpg', cv2.IMREAD_COLOR)
img1 = cv2.imread('./image/add2.jpg', cv2.IMREAD_COLOR)
img_add = cv2.add(img0, img1)
img_sub = cv2.subtract(img0, img1)
img_addwei = cv2.addWeighted(img0, 0.7, img1, 0.3, 0)

cv2.imshow('img0', img0)
cv2.imshow('img1', img1)
cv2.imshow('img_add', img_add)
cv2.imshow('img_sub', img_sub)
cv2.imshow('img_addwei', img_addwei)

cv2.waitKey()