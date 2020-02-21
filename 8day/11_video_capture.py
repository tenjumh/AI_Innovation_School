import cv2 as cv

capture = cv.VideoCapture(1)
width = int(capture.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(capture.get(cv.CAP_PROP_FRAME_HEIGHT))
fps = int(capture.get(cv.CAP_PROP_FPS))
fourcc = cv.VideoWriter_fourcc(*'XVID')
writer = cv.VideoWriter('./image/capture.avi', fourcc, fps, (width, height))

while True:
    ret, frame = capture.read()
    writer.write(frame)
    cv.imshow('frame', frame)
    if cv.waitKey(1) == 27:
        break

capture.release()   # 카메라가 자원을 해제해줌.