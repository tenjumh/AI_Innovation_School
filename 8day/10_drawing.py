import cv2
import numpy as np

img0 = np.zeros((480, 640, 3), np.uint8)
cv2.line(img0, (20, 20), (640, 460), (0, 255, 0), 3)
cv2.rectangle(img0, (100,100), (400,400), (0,0,255), 3)
cv2.rectangle(img0, (500,100), (600,200), (255,0,0), -1)
cv2.ellipse(img0, (240, 320), (300, 200), 0, 0, 360, (0,255,0), 3)
img = np.copy(img0)

def on_mouse(event, x, y, flags, param):
    global img, x0, y0, draw, img0

    if event == cv2.EVENT_LBUTTONDOWN:
        draw = True
        x0, y0 = x, y
    elif draw and event == cv2.EVENT_MOUSEMOVE:
        np.copyto(img, img0)
        cv2.rectangle(img, (x0, y0), (x, y), (0, 255, 0), 3)
    elif event == cv2.EVENT_LBUTTONUP:
        draw = False

cv2.namedWindow('img')
cv2.setMouseCallback('img', on_mouse)

while True:
    cv2.imshow('img', img)
    key = cv2.waitKey(30)
    cv2.imshow('img', img0)
    if key == 27:
        break