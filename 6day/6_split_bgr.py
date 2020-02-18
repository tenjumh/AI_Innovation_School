import cv2

img = cv2.imread('./image/geo.jpg', cv2.IMREAD_UNCHANGED)

b, g, r = cv2.split(img)

cv2.imshow('b', b)
cv2.imshow('g', g)
cv2.imshow('r', r)
cv2.waitKey()