import cv2


image = cv2.imread("food.jpg")

if image is not None:
    resize = cv2.resize(image, (200,250))
    cv2.imshow("Original_image",image)
    cv2.imshow("Resized image", resize)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite("resized_food.jpg", resize)
else:
    print("Image is not loaded")
