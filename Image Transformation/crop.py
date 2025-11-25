
#  imerge[startY:endY, startX,endX]
# Y axis represents row - top to bottom
# X axis represents column - left to right

import cv2

image = cv2.imread("food.jpg")

if image is not None:
    cropped = image[200:400, 150:372]
    cv2.imshow("Cropped Image", cropped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image is not loaded")