import cv2
import numpy as np
# events = [i for i in dir(cv2) if "EVENT" in i]
# print(events)

def click_event(event, x , y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,',' ,y)
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = str(x) + ", "+str(y)
        cv2.putText(img,text, (x,y), font,.5,(10,255,255),1)
        cv2.imshow("Capturing...",img)
    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[y, x, 0]
        green = img[y, x, 1]
        red = img[y, x, 2]
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = str(blue) + ", "+str(green)+", "+str(red)
        cv2.putText(img,text, (x,y), font,.5,(10,255,255),1)
        cv2.imshow("Capturing...",img)
#img = np.zeros((512,512,3),np.uint8)
img = cv2.imread("lena.jpg")
cv2.imshow("Capturing...", img)
points = []
cv2.setMouseCallback("Capturing...",click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()