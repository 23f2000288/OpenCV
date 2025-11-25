import cv2

image = cv2.imread("img.png")


if image is not None:
    h, w, c= image.shape
    print(f"Image is loaded:\nHeight: {h}\nWidth: {w}\nFilter: {c}")
else:
    print("Image is not loaded ! Sorry ")

# Making color image to gray for easy computation:-

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

if gray is not None:

    cv2.imwrite("gray_output_img.png", gray)
    h, w = gray.shape
    print(f"Image is loaded:\nHeight: {h}\nWidth: {w}")
    cv2.imshow("GrayScale image", gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
else:
    print("Image is not gray scaled")

# Now, check shape