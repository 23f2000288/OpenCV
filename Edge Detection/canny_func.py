import cv2

image = cv2.imread("flower.png")

edges = cv2.Canny(image, 50, 100)

cv2.imshow("Original Image",  image)
cv2.imshow("Edges", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()