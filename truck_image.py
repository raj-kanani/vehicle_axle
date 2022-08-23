import cv2
import numpy as np

img = cv2.imread('truck.jpg', 0)
output = img.copy()
img = cv2.medianBlur(img, 5)  # first parameter is image itself, second is kernel size / key size.
cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)  # In this two parameters first is source and second is method.

"""
parameters like image, method, dp, minDist, circles, param1, param2,minradius, maxradius
"""
circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1.1, 220,
                           param1=240,
                           param2=60,
                           minRadius=7,
                           maxRadius=250)

circles = np.uint16(np.around(circles))
for i in circles[0, :]:
    cv2.circle(cimg, (i[0], i[1]), i[2], (255, 0, 0), 2)
    cv2.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 2)

cv2.imshow('circles', cimg)
# cv2.imshow('img cicle', output)
cv2.waitKey(0)
cv2.destroyAllWindows()

