import cv2

def on_mouse(event, x, y, flags, param):
    print(event, x, y, flags, param)

img = cv2.imread('./image/cat.jpg', cv2.IMREAD_UNCHANGED)

cv2.namedWindow('img')
cv2.setMouseCallback('img', on_mouse)

cv2.imshow('img', img)
while True:
    key = cv2.waitKey(30)
    if key == 27: break
