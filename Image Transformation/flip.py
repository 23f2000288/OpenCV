# cv2 flipped(image, flipscale)
# 0 vertically - top to bottom
# 1 horizontally - left to right
# -1 vertically as well as horizontly

import cv2

image = cv2.imread("food.jpg")

if image is not None:
    flip_vertical = cv2.flip(image,0)
    flip_horizonral = cv2.flip(image,1)
    flip_both = cv2.flip(image,-1)
    cv2.imshow("Original_image", image)
    cv2.imshow("Vertical_image", flip_vertical)
    cv2.imshow("Horizontal_image", flip_horizonral)
    cv2.imshow("flip_both_image", flip_both)
    cv2.waitKey()
    cv2.destroyAllWindows()

else:
    print("Image is not loaded")