import numpy as np
import cv2
from func import show_image
#explore cv2.line, cv2.rectangle, cv2. circle

#First Drawing lines and rectangles
canvas = np.zeros((420, 420, 3), dtype='uint8')

green = (0, 255, 0)
red = (0, 0, 255)
white = (255, 250, 255)
yellow = (0, 255, 255)

cv2.line(canvas, (0, 0), (420, 420), green)
cv2.line(canvas, (0, 420), (420, 0), red)
cv2.rectangle(canvas, (10, 10), (60, 60), white, 10)
cv2.rectangle(canvas, (110, 110), (160, 160), yellow, -1)
cv2.rectangle(canvas, (210, 210), (160, 160), yellow, -1)

show_image('Green line', canvas)

#Second drawing only circles
canvas_2 = np.zeros((300, 300, 3), dtype='uint8')
(center_X, center_y) = (canvas_2.shape[1] // 2, canvas_2.shape[0] // 2)
white = (255, 255, 255)

for f in range(0, 150, 25):
    cv2.circle(canvas_2, (center_X, center_y), f, white)

show_image('Circles', canvas_2)

#Third drawing, abstract thing
canvas_3 = np.zeros((500, 500, 3), dtype='uint8')

for i in range(0, 25):
    radius = np.random.randint(5, high=200)
    color = np.random.randint(0, high=256, size=(3, )).tolist()
    pt = np.random.randint(0, high=300, size=(2, ))
    cv2.circle(canvas_3, tuple(pt), radius, color, -1)

show_image('Canvas_3', canvas_3)