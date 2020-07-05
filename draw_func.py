import cv2
import numpy as np



img = np.zeros([512,512,3], np.uint8)
#img = cv2.imread("lena.jpg")
img = cv2.line(img,(0,0),(255,255),(255,0,0),10)
img = cv2.arrowedLine(img,(255,255),(0,255),(0,0,255),10)
img = cv2.rectangle(img,(384,0),(510,128),(0,255,0),1)
img = cv2.circle(img,(255,255),30,(0,63,87),5)
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img,'OpenCV',(10,500),font,4,(25,25,25),10,cv2.LINE_AA)


cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
