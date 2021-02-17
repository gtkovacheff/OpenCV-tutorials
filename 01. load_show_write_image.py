from __future__ import print_function
import cv2

#import image with open cv
image_panda = cv2.imread('images/CutePanda.png')

#explore the image pixels
print('width: {} pixels'.format(image_panda.shape[1]))
print('height: {} pixels'.format(image_panda.shape[0]))
print('channels: {}'.format(image_panda.shape[2]))

#show the image
cv2.imshow('Image', image_panda)
cv2.waitKey(0)

#safe the image in jpg
cv2.imwrite('images/new_panda_image.png', image_panda)