import cv2 as cv


cam = cv.VideoCapture(1)
cam.set(3,640)
cam.set(4,480)


while True:
    _, frame = cam.read()

    cv.imshow('Video', frame)

    key = cv.waitKey(1)
    if key == ord('q'):
        cv.destroyAllWindows()
        break
