import cv2 as cv

capture = cv.VideoCapture('./image/capture.avi')
fps = int(capture.get(cv.CAP_PROP_FPS))
print(fps)

while True:
    ret, frame = capture.read()
    if ret:
        cv.imshow('frame', frame)
    else:
        break
    key = cv.waitKey(fps)
    if key == 27: break

capture.release()