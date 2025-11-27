import numpy as np
import cv2

image = cv2.imread("nature.png")

sharpen_kernal = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])

def img_sharpen(image, sharpen_kernal):
    sharpened = cv2.filter2D(image, -1, sharpen_kernal)
    cv2.imshow("Original Image", image)
    cv2.imshow("Sharpen Image", sharpened)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
img_sharpen(image, sharpen_kernal)


