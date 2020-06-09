import cv2
import time

video = cv2.VideoCapture(0,cv2.CAP_DSHOW)
fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
optput = cv2.VideoWriter("optput.avi",fourcc,30.0,(640,480))
print(video.isOpened())

while video.isOpened():
    check,frame = video.read()
    if check == True:
        print(video.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
        optput.write(frame)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Capturing",gray)
        key = cv2.waitKey(1)
        if key == ord('q'):
           break
    else:
        break
video.release()
optput.release()
cv2.destroyAllWindows()