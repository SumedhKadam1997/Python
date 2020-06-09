import cv2
import numpy as np

def click_event(event, x , y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),3,(0,0,255),-1)
        points.append((x,y))
        if len(points) >= 2:
            cv2.line(img, points[-1],points[-2],(255,0,0),3)

        cv2.imshow("Capturing...", img)

img = np.zeros((512,512,3),np.uint8)
#img = cv2.imread("lena.jpg")
cv2.imshow("Capturing...", img)
points = []
cv2.setMouseCallback("Capturing...",click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()