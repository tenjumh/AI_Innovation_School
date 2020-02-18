import cv2

def on_mouse(event, x, y, flags, param):
    '''
    if event == cv2.EVENT_LBUTTONDOWN:
        print('Left mouse button down at', x, y)
    if event == cv2.EVENT_LBUTTONUP:
        print('Left mouse button down at', x, y)

    if event == cv2.EVENT_LBUTTONDBLCLK:
        print('Left mouse button down at', x, y)

    if event == cv2.EVENT_MOUSEMOVE:
        print('Left mouse button down at', x, y)
    '''
    if event == cv2.EVENT_MOUSEWHEEL:
        if flags == 7864320:
            print('Left mouse WHEEL up at', x, y, flags)
        else:
            print('Left mouse WHEEL down at', x, y, flags)


img = cv2.imread('cat.jpg', cv2.IMREAD_UNCHANGED)

cv2.namedWindow('img')
cv2.setMouseCallback('img', on_mouse)

cv2.imshow('img', img)
cv2.waitKey()
'''
while True:
    key = cv2.waitKey(30)
    if key == 27: break
'''

