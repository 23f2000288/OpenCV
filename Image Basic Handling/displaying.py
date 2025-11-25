import cv2
img = cv2.imread("img.png")

def display_image(image):
    if img is None:
        print("Image is not provided")
    else:
        cv2.imshow("My image",image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
display_image(img)