import cv2
image = cv2.imread("nature.png")

def normal_to_blur(image):

    blurred = cv2.medianBlur(image, 11)

    cv2.imshow("Original", image)
    cv2.imshow("Blurred", blurred)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
normal_to_blur(image)