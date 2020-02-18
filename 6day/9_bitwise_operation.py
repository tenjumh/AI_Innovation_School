import cv2
import numpy as np

img1 = np.zeros((300, 300), np.uint8)
img2 = np.zeros((300, 300), np.uint8)
img3 = np.zeros((300, 300), np.uint8)

cv2.circle(img1, (150, 150), 100, 255, -1)
cv2.rectangle(img2, (0, 0), (150, 300), 255, -1)
cv2.rectangle(img3, (0, 0), (300, 150), 255, -1)

img1_and_img2 = cv2.bitwise_and(img1, img2)
img1_and_img2_mask = cv2.bitwise_and(img1, img2, mask=mask)
img1_or_img2 = cv2.bitwise_or(img1, img2)
img1_xor_img2 = cv2.bitwise_xor(img1, img2)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)
cv2.imshow('img1_and_img2', img1_and_img2)
cv2.imshow('img1_or_img2', img1_or_img2)
cv2.imshow('img1_xor_img2', img1_xor_img2)

cv2.waitKey()
