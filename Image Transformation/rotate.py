# Image Rotation and Flipping


# M = cv2.getRotationMatrix2D(center, angle, scale)
# rotated_image = cv2.warpAffine(image, M, (width,height))
# Center point = (width // 2, height //2)


 

import cv2

image = cv2.imread("food.jpg")

if image is not None:
    (h, w) = image.shape[:2]
    center = (w//2, h//2)
    M = cv2.getRotationMatrix2D(center, 90, 1.0)
    rotated = cv2.warpAffine(image, M, (w,h))
    cv2.imshow("Original_image", image)
    cv2.imshow("Rotated_image by 90 deg", rotated)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite("rotated_img.jpg",rotated)
else:
    print("Image is not loaded")



