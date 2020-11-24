import cv2
import numpy as np
import matplotlib.pyplot as plt

path = '../Data/animals/panda/panda_00001.jpg'
#read the image
image = cv2.imread(path, 0)

#show the image
cv2.imshow('Cute Panda', image)
# cv2.waitKey()
# cv2.destroyAllWindows()

#Write an image
cv2.imwrite('CutePanda.png', image)
cv2.waitKey(0)

#Using matplot lib
keys = (1, -1, 0)
for x in keys:
    pic = cv2.imread(path, x)
    cv2.imshow("Image "+str(x), pic)
#0 for grey scale image, 1, -1 no diff

#diff between opencv and matplotlib
image = cv2.imread(path)
b, g, r = cv2.split(image)
imageRGB = cv2.merge([r, g, b])

plt.subplot(2, 2, 1)
plt.imshow(image)
plt.subplot(2, 2, 2)
plt.imshow(imageRGB)

#using opencv
cv2.imshow('bgr image',image) # expects true color
cv2.imshow('rgb image',imageRGB) # expects distorted color
cv2.waitKey(0)
cv2.destroyAllWindows()