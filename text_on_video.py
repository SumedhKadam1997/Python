import cv2
import datetime

video = cv2.VideoCapture(0)
print(video.get(cv2.CAP_PROP_FRAME_WIDTH))
print(video.get(cv2.CAP_PROP_FRAME_HEIGHT))

# video.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
# video.set(cv2.CAP_PROP_FRAME_HEIGHT,720)

# print(video.get(3))
# print(video.get(4))

while video.isOpened():
    check,frame = video.read()
    if check == True:
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = "WIDTH : "+str(video.get(3)) + "  HEIGHT : "+str(video.get(4))
        date = str(datetime.datetime.now())
        frame = cv2.putText(frame,date,(10,50),font,1,(10,255,255),2,cv2.LINE_AA)
        cv2.imshow('Capturing', frame)
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
    else:
        break


video.release()
cv2.destroyAllWindows()