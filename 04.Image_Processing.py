import numpy as np
import imutils
import cv2
from func import show_image

image = cv2.imread('images/CutePanda.png')
show_image('Panda', image)
M = np.float32([[1, 0, 25], [0, 1, 50]]) #shifting 25 pixels to the right, and 50 pixels down
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
show_image('Shifted Down Right', shifted)

M = np.float32([[1, 0, -50], [0, 1, -90]])#shifting 50 pixels to the left, and 50 pixels up
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
show_image('Shifted Up and Left', shifted)

#Image aritmetic
image
show_image('sth', image)

add_pixel = np.uint8([200])
substract_pixel = np.uint8([50])

cv2.add(substract_pixel, np.uint8([100]))

print(f'max of 255: {cv2.add(add_pixel, np.uint8([100]))}')
print(f'min of 0: {cv2.add(substract_pixel, np.uint8([100]))}')
print(f'wrap around: {add_pixel + np.uint8([100])}')
print(f'wrap around: {substract_pixel - np.uint8([100])}')

# define a matrix that will increase brightness
M = np.ones(image.shape, dtype="uint8") * 100
show_image('matrix', M)
image_added = cv2.add(image, M)
show_image('added', image_added)
image_substracted = cv2.subtract(image, M)
show_image('substracted', image_substracted)

#bitwise
rectangle = np.zeros((300, 300), dtype='uint8')
cv2.rectangle(rectangle, (25, 25), (275, 275), 255, -1)
show_image('masked', rectangle)

circle = np.zeros((300, 300), dtype='uint8')
cv2.circle(circle, (150, 150), 150, 250, -1)
show_image("circle", circle)

# bitwiseAND
bitwiseAND = cv2.bitwise_and(rectangle, circle)
show_image('AND', bitwiseAND)

bitwiseOR = cv2.bitwise_or(rectangle, circle)
show_image('OR', bitwiseOR)

bitwiseXOR = cv2.bitwise_xor(rectangle, circle)
show_image('XOR', bitwiseXOR)

bitwiseNot = cv2.bitwise_not(circle, rectangle)
show_image('Not', bitwiseNot)

#spliting the channels
wave = cv2.imread('images/wave.jpg')
wave.shape
wave =  cv2.resize(wave, (300, 300))
show_image('wave', wave)

(B, G, R) = cv2.split(wave)


cv2.imshow('B', B)
cv2.imshow('G', G)
cv2.imshow('R', R)
cv2.waitKey(0)