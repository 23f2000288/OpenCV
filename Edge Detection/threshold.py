import cv2

image = cv2.imread("flower.png", cv2.IMREAD_GRAYSCALE)

ret, thresh_img = cv2.threshold(image, 100, 200, cv2.THRESH_BINARY)

cv2.imshow("Original Image", image)
cv2.imshow("Thresh Image", thresh_img)
cv2.waitKey(0)
cv2.destroyAllWindows()