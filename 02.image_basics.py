from __future__ import print_function
import cv2
from func import show_image

#read the image
image_panda = cv2.imread('images/CutePanda.png')


#use the function
show_image('Panda', image_panda)

#store bgr values
(b, g, r) = image_panda[0, 0]
print(f'Pixel at (0,0) - Red: {r}, Green: {g}, Blue: {b}')

#manipulate pixel at 0,0 upper left corner
image_panda[0, 0] = (0, 0, 255)
show_image('Image', image_panda)

#cut the upper left corner of the image and show it
corner = image_panda[0:100, 0:100]
show_image('Corner', corner)

# manipulate the upper left corner with green color
image_panda[0:100, 0:100] = (0, 255, 0)
show_image('Updated', image_panda)

