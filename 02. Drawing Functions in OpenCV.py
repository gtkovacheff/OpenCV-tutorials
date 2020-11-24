import numpy as np
import cv2

#Create black images
img = np.zeros((512, 512, 3), np.uint8) + 255

# Drawing Line
line = cv2.line(img, (0, 0), (511, 511), (177, 177, 177), 5)
cv2.imshow('Line', line)

#Drawing Rectangle
rect = cv2.rectangle(img, (0, 0), (128, 128), (25, 25, 255), 3) #top left bottom right
cv2.imshow('Rectangle', rect)

#Drawing Circle
cir = cv2.circle(img, (447, 63), 163, (0, 255, 255), 1)
cv2.imshow('Circle1', cir)

#Drawing Poligon
pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
pts = pts.reshape((-1, 1, 2))
poly = cv2.polylines(img, [pts], True, (0, 0, 255))
cv2.imshow('Polygon', poly)
cv2.waitKey()

#Adding text to images
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV',(10,500), font, 4,(0,255,255),2,cv2.LINE_AA)