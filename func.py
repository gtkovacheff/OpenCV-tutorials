import cv2

#def function to show the image with 1 line of code
def show_image(name, image):
    cv2.imshow(name, image)
    cv2.waitKey(0)